document.getElementById('logout-link').addEventListener('click', function(event) {
  event.preventDefault();  // Prevent the default link behavior (e.g., page refresh)

  // Perform a POST request to the logout URL
  fetch('/logout/', {
    method: 'POST',  // POST request for logout
    headers: {
      'X-CSRFToken': getCookie('csrftoken')  // Include CSRF token
    },
    credentials: 'same-origin'  // Send cookies (session) with the request
  })
  .then(response => {
    if (response.ok) {
      // Redirect to homepage after successful logout
      window.location.href = '/';
    } else {
      alert('Logout failed');
    }
  })
  .catch(error => {
    console.error('Error during logout:', error);
    alert('Logout failed');
  });
});

// Function to get the CSRF token from the cookie
function getCookie(name) {
  const cookieValue = document.cookie.match('(^|;)\\s*' + name + '=([^;]+)');
  return cookieValue ? cookieValue.pop() : '';
}
