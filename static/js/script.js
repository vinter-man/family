async function uploadFile() {
  const fileInput = document.getElementById("fileInput");
  if (fileInput.files.length === 0) {
    alert("Select file to upload");
    return;
  }

  const formData = new FormData();
  formData.append("file", fileInput.files[0]);

  const response = await fetch("/upload", { method: "POST", body: formData });
  const result = await response.json();

  if (response.status !== 200) {
    alert("Error: " + result.errors.join(", "));
    return;
  }

  // Successful upload
  document.querySelector(".upload-section").style.display = "none";
  document.getElementById("tree-container").style.display = "block";
  renderFamilyTree(result.data);
}

function renderFamilyTree(data) {
  const canvas = document.getElementById("treeCanvas");
  const ctx = canvas.getContext("2d");
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Generate tree on canvas
  // Logic for building tree nodes, lines and scaling control
  // Example tree structure
  ctx.fillStyle = "#1e90ff";
  data.forEach((member) => {
    // We draw nodes for each family member, setting up according to their coordinates on the canvas
    ctx.fillRect(member.x, member.y, 150, 50); // Approximate rectangle
    ctx.fillStyle = "#fff";
    ctx.fillText(member.name, member.x + 10, member.y + 20);
    // Logic for handling children, parents and relationships
  });
}
