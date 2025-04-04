import os
import sys
import platform
import glob


def rename_wheel():
    # Get the current platform
    current_platform = platform.system().lower()

    # Find the wheel file in the dist directory
    wheel_files = glob.glob('dist/*.whl')

    if not wheel_files:
        print("No wheel file found in the dist directory.")
        sys.exit(1)

    # Get the first wheel file (assuming there's only one in the dist directory)
    wheel_file = wheel_files[0]
    base_name = os.path.basename(wheel_file)

    # Split the base name into components
    name_parts = base_name.split('-')

    # Platform-specific suffix for the wheel file
    if current_platform == "linux":
        suffix = "manylinux1_x86_64"
    elif current_platform == "windows":
        suffix = "win_amd64"
    elif current_platform == "darwin":
        suffix = "macosx_10_9_x86_64"
    else:
        print(f"Unsupported platform: {current_platform}")
        sys.exit(1)

    name_parts[-1] = f"{suffix}.whl"

    # Construct the new wheel file name
    new_wheel_name = '-'.join(name_parts)

    # Rename the wheel file
    os.rename(wheel_file, os.path.join('dist', new_wheel_name))
    print(f"Wheel renamed to: {new_wheel_name}")


if __name__ == "__main__":
    rename_wheel()
