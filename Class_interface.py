import customtkinter as ctk

#-----------------------------------------------------------------------------------------------------------------------------------------#
#                                                  CREATION DE LA CLASSE FENETRE                                                          # 
#-----------------------------------------------------------------------------------------------------------------------------------------#

class App(ctk.CTk):
    def __init__(self,Title='New Windows',Theme=''):
        super().__init__()

        ##-- Definition des attributs de la classe
        self.title(Title)
        self._set_appearance_mode(Theme)
       

        ##-- Apparence des fenetres

        # Selecting GUI theme - dark, light , system (for system default)
        





