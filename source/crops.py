import pymupdf, sys
R="D:/projects/swe2-PastPapers/Exams/"
C = {
 "F24c_cfg":   ("Final/2024/final_3nd_2024.pdf", 5, (0.33,0.17,0.68,0.39)),
 "M24c_usecase":("Midterm/2024/Midterm-3rd-2024.pdf", 7, (0.05,0.64,0.88,0.99)),
 "F23b_misuse":("Final/2023/_Final_2nd_CS392_2023.pdf", 6, (0.08,0.485,0.80,0.91)),
 "M22_seq":    ("Midterm/2021/Midterm1_2021_Answers.pdf", 3, (0.12,0.27,0.65,0.775)),
 "F21_cfg":    ("Final/2021/Final2021_ModelAnswer.pdf", 5, (0.145,0.385,0.645,0.572)),
}
only = sys.argv[1:] or list(C)
for k in only:
    f,p,(x0,y0,x1,y1) = C[k]
    page = pymupdf.open(R+f)[p-1]
    r = page.rect
    clip = pymupdf.Rect(r.x0+x0*r.width, r.y0+y0*r.height, r.x0+x1*r.width, r.y0+y1*r.height)
    pix = page.get_pixmap(dpi=150, clip=clip)
    pix.save(f"img/{k}.jpg", jpg_quality=82); print(k, pix.width, pix.height)
