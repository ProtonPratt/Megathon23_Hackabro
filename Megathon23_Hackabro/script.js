function submitForm() {
    // Get values from form
    var form = document.getElementById('socialMediaForm');
    var twitterHandle = document.getElementById('twitter').value;
    var linkedinHandle = document.getElementById('linkedin').value;
    var imdbIndicator = document.getElementById('imdb').value;
  
    // Check if any field is empty
    if (!twitterHandle || !linkedinHandle || !imdbIndicator) {
      alert('Please fill in all fields.');
      return; // Stop form submission
    }
  
    // If all fields are filled, proceed with form submission
    // You can add additional logic here if needed
    // alert('Form submitted!');
    
    var formData = {
        twitter: twitterHandle,
        linkedin: linkedinHandle,
        imdb: imdbIndicator
      };

    fetch('http://127.0.0.1:5000/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })

  }
   