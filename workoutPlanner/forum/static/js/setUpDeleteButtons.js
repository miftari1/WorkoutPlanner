function getCSRFToken() {
      const cookies = document.cookie.split(';');
      for (let cookie of cookies) {
        if (cookie.trim().startsWith('csrftoken=')) {
          return cookie.trim().split('=')[1];
        }
      }
      return '';
}


const posts = document.querySelectorAll('.post-container');
const host = '/api/posts'; // Leading slash ensures correct relative path

for (let post of posts) {
    let button = post.querySelector('.delete-post');
    button.addEventListener('click', async () => {
        const postId = button.dataset.postId;
        await deletePost(postId, post);
    });
}

async function deletePost(id, element) {
    try {
        const response = await fetch(`${host}/${id}/`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken()
            }
        });

        if (!response.ok) {
            throw new Error('Failed to delete post.');
        }

        element.remove();

    } catch (error) {
        console.error('Error deleting post:', error);
    }
}