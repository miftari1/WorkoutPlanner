
function getCSRFToken() {
      const cookies = document.cookie.split(';');
      for (let cookie of cookies) {
        if (cookie.trim().startsWith('csrftoken=')) {
          return cookie.trim().split('=')[1];
        }
      }
      return '';
}

const showBtn = document.getElementById('show-add-post-btn');
const form = document.getElementById('add-post-form');
const hideBtn = document.getElementById('hide-form-btn');
const postList = document.getElementById('post-list');

showBtn.addEventListener('click', () => form.style.display = 'block');
hideBtn.addEventListener('click', () => form.style.display = 'none');

document.getElementById('submit-post').addEventListener('click', () => {
  const title = document.getElementById('post-title').value.trim();
  const body = document.getElementById('post-body').value.trim();

  if (!title || !body) {
    alert("Please enter both title and body.");
    return;
  }

  fetch('/api/posts/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': getCSRFToken()
    },
    body: JSON.stringify({ title, body })
  })
  .then(async res => {
    if (!res.ok) {
      throw new Error(`HTTP error! status: ${res.status}`);
    }
    return res.json();
  })
  .then(data => {
    // Add the new post to the page
    const newPost = document.createElement('div');
    newPost.className = 'post-container';
    newPost.innerHTML = `
      <h2>
        <a href="{% url 'forum:post_detail' pk=post.pk %}">
            ${data.title}
        </a>
        <div class="post-btn-container">
          <a href="#" class="delete-post-btn">Edit post</a>
          <a href="#" class="delete-post-btn">Delete post</a>
        </div>
      </h2>
      <p class="date">
        Published just now by You.
      </p>
      <div class="content">
        ${data.body}
      </div >
    `;

    postList.prepend(newPost);

    // Clear and hide the form
    document.getElementById('post-title').value = '';
    document.getElementById('post-body').value = '';
    form.style.display = 'none';
  })
  .catch(err => {
    console.error(err);
    alert('Error creating post.');
  });
});