$(document).ready(function() {
    const video = document.getElementById('video');
    const canvas = document.getElementById('canvas');
    const context = canvas.getContext('2d');
    const capturedImg = document.getElementById('capturedImg');
    const captureBtn = document.getElementById('captureBtn');
    const approveBtn = document.getElementById('approveBtn');
    const rejectBtn = document.getElementById('rejectBtn');

    navigator.mediaDevices.getUserMedia({ video: true })
    .then(function(stream) {
        video.srcObject = stream;
    })
    .catch(function(err) {
        console.error('Error accessing webcam: ', err);
    });

    captureBtn.addEventListener('click', function() {
        context.drawImage(video, 0, 0, 640, 480);
        capturedImg.src = canvas.toDataURL('image/jpeg');
        capturedImg.style.display = 'block';
        approveBtn.style.display = 'block';
        rejectBtn.style.display = 'block';
    });

    approveBtn.addEventListener('click', function() {
        // Logic to save image
    });

    rejectBtn.addEventListener('click', function() {
        // Logic to discard image
    });
});
