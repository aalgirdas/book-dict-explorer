

import requests, json

# Fetch dictionary from GitHub
def load_book_dict():
    url = "https://raw.githubusercontent.com/aalgirdas/novel-semantic-parsing/refs/heads/main/file_path_dic.json"
    return json.loads(requests.get(url).text)


def search_books(query: str):
    """
    Return list of (book_name, metadata) matching `query` in name or code.
    """
    dic = load_book_dict()
    results = []
    for name, meta in dic.items():
        if query.lower() in name.lower() or query == meta.get("book_code", ""):
            results.append((name, meta))
    if not results:
        return "No matches found."
    # Format output as Markdown or plain text
    return "\n\n".join(f"**{n}** → `{m}`" for n, m in results)



import gradio as gr

with gr.Blocks(title="Book Dictionary Explorer") as demo:
    gr.Markdown("## 🔍 Search your books by title or code")
    query = gr.Textbox(label="Enter title or code")
    output = gr.Markdown()
    query.submit(fn=search_books, inputs=query, outputs=output)

if __name__ == "__main__":
    demo.launch()