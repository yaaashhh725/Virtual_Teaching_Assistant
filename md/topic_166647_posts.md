# i-have-doubt-in-q10

**post_id:** 592777  
**author:** 23f1001806  
**timestamp:** 2025-02-09T14:51:52.566Z

# i-have-doubt-in-q10

I have doubt in question 10 to convert pdf to markdown  
I am not getting correct markdown  
[@pds\_staff](/u/pds_staff)

---

**post_id:** 593235  
**author:** 22f3000092  
**timestamp:** 2025-02-09T18:15:12.582Z

Try using the pymupdf4llm Library  
pip install pymupdf4llm

import pymupdf4llm  
md\_text = pymupdf4llm.to\_markdown(“input.pdf”)

import pathlib  
pathlib.Path(“output.md”).write\_bytes(md\_text.encode())

import pymupdf4llm  
llama\_reader = pymupdf4llm.LlamaMarkdownReader()  
llama\_docs = llama\_reader.load\_data(“input.pdf”)

---

