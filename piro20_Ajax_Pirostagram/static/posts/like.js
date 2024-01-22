const requestLike = new XMLHttpRequest();

const onClickLike = (id, type) => {
    const url = "/like_ajax/";
    requestLike.open("POST", url, true);
    requestLike.setRequestHeader(
        "Content-Type",
        "application/x-www-form-urlencoded"
    );
    requestLike.send(JSON.stringify({id: id, type: type}));
}
requestLike.onreadystatechange = () => {
    if (requestLike.readyState === XMLHttpRequest.DONE) {
        if (requestLike.status < 400) {
            const {id, type} = JSON.parse(requestLike.response);
            const element = document.querySelector(`.post-id-${id} .post__${type}`);
            const originHTML = element.innerHTML;
            const [buttonType, num] = originHTML.split(" ");
            const count = Number(num) + 1;

            element.innerHTML = `${buttonType} ${count}`;
        }
    }
}

const requestComment = new XMLHttpRequest();
const onSubmitComment = (id) => {
    const url = "comment/";
    const commentInput = document.getElementById(`commentInput-${id}`).value;
    requestComment.open("POST", url, true);
    requestComment.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    requestComment.onreadystatechange = () => {
        if (requestComment.readyState === XMLHttpRequest.DONE) {
            if (requestComment.status < 400) {
                console.log("댓글이 등록되었습니다.");
                getComments(id);
            } else {
                console.error("댓글 등록에 실패했습니다.");
            }
        }
    };
    requestComment.send(JSON.stringify({id:id, comment: commentInput}))
}

const getComments = (postId) => {
    const commentListContainer = document.getElementById(`commentList-${postId}`);
    const url = `get_comments/${postId}/`;

    const requestComments = new XMLHttpRequest();
    requestComments.open("GET", url, true);
    requestComments.onreadystatechange = () => {
        if (requestComments.readyState === XMLHttpRequest.DONE) {
            if (requestComments.status < 400) {
                const comments = JSON.parse(requestComments.response);
                commentListContainer.innerHTML = comments.map(comment => `
                    <p>${comment.content} 
                        <button onclick="onDeleteComment(${postId}, ${comment.id})">삭제</button>
                    </p>`).join('');
            }
        }
    };
    requestComments.send();
};

const onDeleteComment = (postId, commentId) => {
    const url = `delete_comment/${postId}/${commentId}/`;

    const requestDeleteComment = new XMLHttpRequest();
    requestDeleteComment.open("POST", url, true);
    requestDeleteComment.onreadystatechange = () => {
        if (requestDeleteComment.readyState === XMLHttpRequest.DONE) {
            if (requestDeleteComment.status < 400) {
                console.log("댓글이 삭제되었습니다.");
                getComments(postId);
            } else {
                console.error("댓글 삭제에 실패했습니다.");
            }
        }
    };
    requestDeleteComment.send();
};
