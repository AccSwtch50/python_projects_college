def preview_post(post_content):
    if len(post_content) <= 140:
        return (post_content, False)
    post_trunc = post_content[:139] + "..."
    return (post_trunc, True)

def main():
    post = input("Post: ")
    preview_post_object = preview_post(post)
    print(preview_post_object[0])
    if preview_post_object[1]:
        print("This post cannot be posted because it is too long, try shortening it.")

main()