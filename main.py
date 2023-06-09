import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

entry = None
resultado_label = None
detective_label = None
imagem_label = None
imagem_original = None
imagem_detetive = None

def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    
    mid = len(arr) // 2
    left, inv_left = merge_sort(arr[:mid])
    right, inv_right = merge_sort(arr[mid:])
    merged, inv_split = merge(left, right)
    
    inversions = inv_left + inv_right + inv_split
    return merged, inversions

def merge(left, right):
    merged = []
    inversions = 0
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            inversions += len(left) - i
    
    while i < len(left):
        merged.append(left[i])
        i += 1
    
    while j < len(right):
        merged.append(right[j])
        j += 1
    
    return merged, inversions

def count_inversions(arr):
    _, inversions = merge_sort(arr)
    return inversions

def exibir_janela_sem_numeros():
    janela_sem_numeros = tk.Toplevel()
    janela_sem_numeros.title("Erro na Investigação")
    janela_sem_numeros.geometry("300x150")
    mensagem_label = ttk.Label(janela_sem_numeros, text="Nenhum número foi inserido.\n"
                                                        "Digite uma sequência numérica\n"
                                                        "para continuar.", 
                              font=("Arial", 12))
    mensagem_label.pack(pady=20)
    fechar_button = ttk.Button(janela_sem_numeros, text="Fechar", command=janela_sem_numeros.destroy)
    fechar_button.pack()

def verificar_inversoes():
    global entry, resultado_label, detective_label

    numeros = entry.get()

    if not numeros:
        exibir_janela_sem_numeros()
        return

    numeros = numeros.split()
    numeros = [int(num) for num in numeros]

    inversoes = count_inversions(numeros)
    
    detective_label.config(text=f"Sequência de números: {numeros}")
    resultado_label.config(text=f"Número de inversões: {inversoes}")

    if inversoes == 0:
        detective_label.config(text="Essa sequência não possui inversões. O detetive agradece sua colaboração!")
    else:
        detective_label.config(text="Essa sequência possui inversões. O detetive investigará mais a fundo!")

def resize_image(event):
    global imagem_original, imagem_label, imagem_detetive

    nova_largura = event.width
    nova_altura = event.height

    imagem_redimensionada = imagem_original.resize((nova_largura, nova_altura), Image.ANTIALIAS)
    imagem_detetive = ImageTk.PhotoImage(imagem_redimensionada)

    imagem_label.config(image=imagem_detetive)

def abrir_janela_principal():
    global entry, resultado_label, detective_label

    janela_inicial.destroy()

    janela = tk.Tk()
    janela.title("Jogo do Detive - Investigação")
    janela.geometry("600x300")

    titulo_label = ttk.Label(janela, text="Caso 004 - Contagem de Inversões!", font=("Arial", 16, "bold"))
    instrucao_label = ttk.Label(janela, text="Você precisa digitar uma sequência de números separados por espaços\n"
                                             "para que o detetive possa seguir com a sua investigação. Lembre-se que\n"
                                             "você pode dar uma sequência já ordenada ou não.", 
                                font=("Arial", 12))
    entry = ttk.Entry(janela, font=("Arial", 12))
    verificar_button = ttk.Button(janela, text="Verificar", command=verificar_inversoes)
    resultado_label = ttk.Label(janela, text="", font=("Arial", 12))
    detective_label = ttk.Label(janela, text="", font=("Arial", 12))

    titulo_label.pack(pady=10)
    instrucao_label.pack()
    entry.pack(pady=10)
    verificar_button.pack(pady=10)
    resultado_label.pack()
    detective_label.pack(pady=10)

    janela.mainloop()
    
def aumentar_texto(event):
    # Função para aumentar o tamanho da fonte do texto
    global texto_label

    nova_tamanho_fonte = max(int(event.width / 40), 10)
    texto_label.configure(font=("Arial", nova_tamanho_fonte, "bold"))
    
def abrir_janela_inicial():
    global janela_inicial, imagem_original, imagem_detetive, imagem_label

    janela_inicial = tk.Tk()
    janela_inicial.title("Jogo do Detetive - Início")
    janela_inicial.geometry("800x600+10+10")

    imagem_original = Image.open("assets/detetive.png")
    imagem_detetive = ImageTk.PhotoImage(imagem_original)
    imagem_label = ttk.Label(janela_inicial, image=imagem_detetive)
    imagem_label.pack(expand=True, fill="both")
    
    texto_label = ttk.Label(janela_inicial, text="O renomado detetive Ryan Donovan precisa da sua\n"
                                                 "ajuda para solucionar uma das pistas de um caso\n"
                                                 "que acaba de surgir. Clique em 'Iniciar' para a\n"
                                                 "aventura começar e boa sorte!",
                       font=("Arial", 14, "bold"))
    texto_label.configure(background='white')
    texto_label.place(relx=0.38, rely=0.40, anchor="center")
    
    iniciar_button = ttk.Button(janela_inicial, text="Iniciar", command=abrir_janela_principal)
    iniciar_button.place(relx=0.45, rely=0.60, anchor="center")

    janela_inicial.resizable(True, True)
    janela_inicial.bind("<Configure>", resize_image)

    janela_inicial.mainloop()

abrir_janela_inicial()