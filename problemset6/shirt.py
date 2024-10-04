import sys
from PIL import Image, ImageOps

def main():
    # Ensure correct number of arguments
    if len(sys.argv) != 3:
        print("Usage: shirt.py input_image output_image")
        sys.exit(1)

    input_image = sys.argv[1]
    output_image = sys.argv[2]

    # Ensure input and output have valid extensions
    valid_extensions = [".jpg", ".jpeg", ".png"]
    input_ext = input_image.lower().split('.')[-1]
    output_ext = output_image.lower().split('.')[-1]

    if input_ext not in valid_extensions or output_ext not in valid_extensions:
        print("Error: Invalid file type. Please use .jpg, .jpeg, or .png.")
        sys.exit(1)

    # Ensure input and output have the same extension
    if input_ext != output_ext:
        print("Error: Input and output file extensions must match.")
        sys.exit(1)

    # Try to open the input image and overlay the shirt
    try:
        # Open the input image
        input_img = Image.open(input_image)

        # Open the shirt image
        shirt_img = Image.open("shirt.png")

        # Resize and crop the input image to match the shirt size
        resized_img = ImageOps.fit(input_img, shirt_img.size)

        # Overlay the shirt image on the resized input image
        resized_img.paste(shirt_img, shirt_img)

        # Save the result
        resized_img.save(output_image)

    except FileNotFoundError:
        print(f"Error: {input_image} not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
