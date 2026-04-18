const projects = [
    {
        title: "Quiz Master AI",
        folder: "Project1_Study_Notes_to_Quiz",
        images: ["Gambar1.png", "Gambar2.png", "Gambar3.png", "Gambar4.png"]
    },
    {
        title: "RPP Generator Pro",
        folder: "Project2_Penyusun_RPP_Digital",
        images: ["Gambar1.png", "Gambar2.png", "Gambar3.png", "Gambar4.png", "Gambar5.png", "Gambar6.png"]
    },
    {
        title: "AI Essay Grader",
        folder: "Project3_Asisten_Penilai_Esai",
        images: ["Gambar1.png", "Gambar2.png", "Gambar3.png", "Gambar4.png", "Gambar5.png"]
    }
];

let currentProjectIndex = -1;
let currentImageIndex = 0;

const lightbox = document.getElementById('lightbox');
const lightboxImg = document.getElementById('lightboxImg');
const lightboxTitle = document.getElementById('lightboxTitle');
const lightboxThumbs = document.getElementById('lightboxThumbs');

function openGallery(index) {
    currentProjectIndex = index;
    currentImageIndex = 0;
    
    const project = projects[index];
    lightboxTitle.innerText = project.title;
    
    updateLightboxImage();
    renderThumbnails();
    
    lightbox.classList.add('active');
    document.body.style.overflow = 'hidden'; // Prevent scrolling
}

function closeGallery() {
    lightbox.classList.remove('active');
    document.body.style.overflow = 'auto';
}

function updateLightboxImage() {
    const project = projects[currentProjectIndex];
    const imageName = project.images[currentImageIndex];
    lightboxImg.src = `${project.folder}/${imageName}`;
    
    // Update active thumbnail
    const thumbs = document.querySelectorAll('.thumb-item');
    thumbs.forEach((t, i) => {
        if (i === currentImageIndex) t.classList.add('active');
        else t.classList.remove('active');
    });
}

function renderThumbnails() {
    const project = projects[currentProjectIndex];
    lightboxThumbs.innerHTML = '';
    
    project.images.forEach((img, i) => {
        const thumb = document.createElement('img');
        thumb.src = `${project.folder}/${img}`;
        thumb.classList.add('thumb-item');
        if (i === 0) thumb.classList.add('active');
        
        thumb.onclick = () => {
            currentImageIndex = i;
            updateLightboxImage();
        };
        
        lightboxThumbs.appendChild(thumb);
    });
}

// Close lightbox on click outside content
lightbox.onclick = function(e) {
    if (e.target === lightbox) {
        closeGallery();
    }
};

// Keyboard navigation
document.addEventListener('keydown', (e) => {
    if (!lightbox.classList.contains('active')) return;
    
    if (e.key === 'Escape') closeGallery();
    if (e.key === 'ArrowRight') {
        currentImageIndex = (currentImageIndex + 1) % projects[currentProjectIndex].images.length;
        updateLightboxImage();
    }
    if (e.key === 'ArrowLeft') {
        currentImageIndex = (currentImageIndex - 1 + projects[currentProjectIndex].images.length) % projects[currentProjectIndex].images.length;
        updateLightboxImage();
    }
});
