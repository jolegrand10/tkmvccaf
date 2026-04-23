""" Module viewcaf.py pour la Classe Vue de l'application CAF"""


import tkinter as tk

class ViewCaf:

    def __init__(self):
        #
        # creer une fenêtre
        #
        win = tk.Tk()
        self.win = win
        #
        # mettre un titre
        #
        win.title("Calcul de votre allocation familiale")
        #
        # remplir la vue avec des widgets
        #
        self.make_widgets()
    
    def make_widgets(self):
        #
        # mettre un label "Votre salaire"
        #
        label_salaire = tk.Label(self.win, text="Votre salaire")
        label_salaire.pack()
        #
        # Mettre un champ de saisie pour le salaire
        #
        self.entry_salaire = tk.Entry(self.win, )
        self.entry_salaire.pack()
        #
        # mettre un label " Votre allocation"
        #
        label_allocation = tk.Label(self.win, text="Votre allocation")
        label_allocation.pack()
        #
        # mettre un champ d'affichage pour l'allocation
        #
        self.label_valeur = tk.Label(self.win, text="0.00")
        self.label_valeur.pack()
        #
        # mettre un bouton Calcul
        #
        self.button_calcul = tk.Button(self.win, text="Calcul",)
        self.button_calcul.pack()
        #
        # mettre un bouton RAZ
        # 
        button_raz = tk.Button(self.win, text="RAZ",command=self.raz)
        button_raz.pack()
        #
        # mettre un bouton Quitter
        #
        button_quitter = tk.Button(self.win, text="Quitter", command=self.win.destroy)
        button_quitter.pack()
    
    def raz(self):
        print("On remet tout à Zéro")
        self.label_valeur.config(text=" ")
        self.entry_salaire.delete(0, tk.END)
    
    def set_command_calcul(self, fn):
        self.button_calcul.config(command=fn)
    
    def get_salaire(self):
        return float(self.entry_salaire.get())
    
    def set_allocation(self, v):
        self.label_valeur.config(text=v)

    def run(self):
        #
        # Boucle principale d'événements
        #
        self.win.mainloop()

def main():
    vc = ViewCaf()
    vc.run()


if __name__ == "__main__":
    main()