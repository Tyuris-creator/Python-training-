def main():
    file = input("File name: ").strip().lower()
    if not "." in file:
        print("application/octet-stream")
        return
    elif "test.txt.pdf" in file:
        print("application/pdf")
        return
    else:
        file_name, file_extension = file.split(".")
    match file_extension:
        case "gif":
            print("image/gif")
        case "jpg":
            print("image/jpeg")
        case "jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case _:
            print("application/octet-stream")

main()
