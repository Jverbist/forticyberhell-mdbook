// -- CHANGE BORDER COLOR: attacker = red VS defender = blue
document.addEventListener("DOMContentLoaded", function () {
    // Get the current URL path
    let path = window.location.pathname.toLowerCase();

    // Extract the markdown file name
    let fileName = path.substring(path.lastIndexOf("/") + 1);

    // Find the main content area in mdBook
    let pageContent = document.querySelector(".page");

    if (pageContent) {
        if (fileName.includes("attacker")) {
            pageContent.style.borderLeft = "5px solid red"; // Red for attackers
        } else if (fileName.includes("defender")) {
            pageContent.style.borderLeft = "5px solid #276FBC"; // Blue for defenders
        }
    }
});

// -- OPEN LINKS/URLs in new Browser Tab
document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("a[href]").forEach(function (link) {
        if (link.hostname !== window.location.hostname) {
            link.target = "_blank";
            link.rel = "noopener noreferrer";
        }
    });
});
// -- OPEN Pictures/Images in FULL SCREEN with Zoom Controls and a Close Button
document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("img").forEach(img => {
        img.style.cursor = "zoom-in";
        img.addEventListener("click", function () {
            const overlay = document.createElement("div");
            overlay.style.position = "fixed";
            overlay.style.top = 0;
            overlay.style.left = 0;
            overlay.style.width = "100vw";
            overlay.style.height = "100vh";
            overlay.style.backgroundColor = "rgba(0, 0, 0, 0.85)";
            overlay.style.display = "flex";
            overlay.style.flexDirection = "column";
            overlay.style.justifyContent = "center";
            overlay.style.alignItems = "center";
            overlay.style.zIndex = 9999;
            overlay.style.overflow = "hidden";

            let zoomLevel = 1;

            // Create the buttons container FIRST
            const controls = document.createElement("div");
            controls.style.position = "fixed"; // <== fixed, so it stays in place!
            controls.style.top = "20px";
            controls.style.right = "20px";
            controls.style.display = "flex";
            controls.style.gap = "10px";
            controls.style.zIndex = 10000; // <== higher than the image
            controls.style.background = "rgba(255, 255, 255, 0.8)";
            controls.style.padding = "8px";
            controls.style.borderRadius = "8px";
            controls.style.boxShadow = "0 0 10px rgba(0, 0, 0, 0.5)";

            // Helper function to create styled buttons
            function createButton(text, onClick) {
                const button = document.createElement("button");
                button.innerText = text;
                button.style.padding = "8px 12px";
                button.style.fontSize = "18px";
                button.style.cursor = "pointer";
                button.style.border = "2px solid #333";
                button.style.borderRadius = "5px";
                button.style.background = "#ffffff";
                button.style.color = "#333";
                button.style.fontWeight = "bold";
                button.addEventListener("click", function (e) {
                    e.stopPropagation();
                    onClick();
                });
                return button;
            }

            // Create Zoom In button
            const zoomIn = createButton("+", () => {
                zoomLevel += 0.2;
                fullImage.style.transform = `scale(${zoomLevel})`;
            });

            // Create Zoom Out button
            const zoomOut = createButton("-", () => {
                zoomLevel = Math.max(0.2, zoomLevel - 0.2);
                fullImage.style.transform = `scale(${zoomLevel})`;
            });

            // Create Close button
            const closeButton = createButton("✖️", () => {
                document.body.removeChild(overlay);
            });

            // Append all buttons
            controls.appendChild(zoomIn);
            controls.appendChild(zoomOut);
            controls.appendChild(closeButton);

            // Now create the image AFTER the buttons are set
            const fullImage = document.createElement("img");
            fullImage.src = this.src;
            fullImage.style.maxWidth = "95%";
            fullImage.style.maxHeight = "95%";
            fullImage.style.boxShadow = "0 0 15px black";
            fullImage.style.transition = "transform 0.3s ease";

            overlay.appendChild(controls);
            overlay.appendChild(fullImage);
            document.body.appendChild(overlay);

            // Also close overlay if clicking outside (optional)
            overlay.addEventListener("click", (e) => {
                if (e.target === overlay) {
                    document.body.removeChild(overlay);
                }
            });
        });
    });
});
