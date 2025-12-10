import cv2
import numpy as np
from pathlib import Path
from tqdm import tqdm

def create_lowlight(image, method='mixed'):
    """
    Create synthetic low-light images using various methods
    method: 'exposure', 'gamma', 'mixed'
    """
    if method == 'exposure':
        # Simple exposure reduction (multiply by factor)
        factor = np.random.uniform(0.1, 0.4)
        darkened = (image * factor).astype(np.uint8)
        param = factor
        
    elif method == 'gamma':
        # Gamma correction (>1 darkens)
        gamma = np.random.uniform(1.8, 3.0)
        darkened = np.power(image / 255.0, gamma)
        darkened = (darkened * 255).astype(np.uint8)
        param = gamma
        
    else:  # mixed
        # Combine both methods
        factor = np.random.uniform(0.15, 0.45)
        gamma = np.random.uniform(1.2, 2.0)
        darkened = np.power((image * factor) / 255.0, gamma)
        darkened = (darkened * 255).astype(np.uint8)
        param = (factor, gamma)
    
    return darkened, param

# Setup paths
gt_dir = Path("project/code/datasets/ground_truth")
ll_dir = Path("project/code/datasets/low_light")

print(f"Ground truth dir: {gt_dir.absolute()}")
print(f"Exists: {gt_dir.exists()}")

if gt_dir.exists():
    all_files = list(gt_dir.iterdir())
    print(f"Total files in directory: {len(all_files)}")
    if all_files:
        print(f"First few files: {[f.name for f in all_files[:5]]}")
else:
    print("ERROR: Ground truth directory doesn't exist!")
    exit(1)

ll_dir.mkdir(parents=True, exist_ok=True)

# Process all images
image_extensions = ["*.jpg", "*.jpeg", "*.png", "*.JPG", "*.JPEG", "*.PNG"]
image_files = [f for ext in image_extensions for f in gt_dir.glob(ext)]

print(f"\nFound {len(image_files)} image files")

for img_path in tqdm(image_files, desc="Creating low-light images"):
    img = cv2.imread(str(img_path))
    if img is not None:
        lowlight, param = create_lowlight(img, method='exposure')
        cv2.imwrite(str(ll_dir / img_path.name), lowlight)
        if isinstance(param, tuple):
            tqdm.write(f"{img_path.name}: factor={param[0]:.2f}, γ={param[1]:.2f}")
        else:
            tqdm.write(f"{img_path.name}: {param:.2f}")

print(f"\nDone! Created {len(list(ll_dir.glob('*')))} low-light images")