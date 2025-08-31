import os
import subprocess

# === CONFIG ===
CLEAN_DIR = "data/clean"
GT_DIR = "data/gt"
OUT_DIR = "data/gt/train"
LANG = "aho"  # language code for Ahom
os.makedirs(OUT_DIR, exist_ok=True)

def generate_training_files():
    for file in os.listdir(CLEAN_DIR):
        if file.endswith(".png"):
            base = os.path.splitext(file)[0]   # e.g., page_1
            img_path = os.path.join(CLEAN_DIR, file)
            txt_path = os.path.join(GT_DIR, f"{base}.txt")

            if not os.path.exists(txt_path):
                print(f"[!] Missing GT for {file}, skipping...")
                continue

            out_base = os.path.join(OUT_DIR, base)

            
            cmd = [
                "tesseract",
                img_path,
                out_base,
                "nobatch",
                "box.train",
                f"-l {LANG}"
            ]
            print(" ".join(cmd))
            subprocess.run(" ".join(cmd), shell=True)

            print(f"[+] Training files generated for {file}")

if __name__ == "__main__":
    generate_training_files()
    print("\n✅ All training files generated in data/gt/train/")