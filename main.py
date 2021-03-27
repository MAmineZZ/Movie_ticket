import datetime
import tkinter
import csv
from tkinter import messagebox, ttk, N, W, E


class evenement:
    num = None
    date_dif = None
    nom = None
    salle_eve = None
    nb_palces_reserevees = None

    def __init__(self, num, date_dif, nom, salle_eve, nb_palces_reserevees):
        self.num = num
        self.date_dif = date_dif
        self.nom = nom
        self.salle_eve = salle_eve
        self.nb_palces_reserevees = nb_palces_reserevees


class personne:
    id_pers = None
    user_name = None
    user_mdp = None
    user_statut = None

    def __init__(self, id_pers, user_name, user_mdp, user_statut):
        self.id_pers = id_pers
        self.user_name = user_name
        self.user_mdp = user_mdp
        self.user_statut = user_statut


def login():
    user_nm = personne.user_name.get()
    user_mp = personne.user_mdp.get()
    with open('test.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['user'] == user_nm and row['user_mdp'] == user_mp:
                personne.user_statut = 1
                fenetre_identification.iconify()
                ouvrir_fenetre_gestion()
            elif row['admin'] == user_nm and row['admin_mdp'] == user_mp:
                personne.user_statut = 2
                fenetre_identification.iconify()
                ouvrir_fenetre_gestion()

            elif row['client'] == user_nm and row['client_mdp'] == user_mp:
                personne.user_statut = 3
                fenetre_identification.iconify()
                ouvrir_fenetre_gestion()
            else:
                tkinter.messagebox.askretrycancel(title='Données erronés', message='Réssayer')


def ouvrir_fenetre_gestion():
    global fenetre_gestion
    fenetre_gestion = tkinter.Toplevel(fenetre_identification)
    fenetre_gestion.title('Fentre gestion')
    fenetre_gestion.geometry('500x150')
    titre_gest = tkinter.Label(fenetre_gestion, text='Bienvenue au gestion', width=70)
    titre_gest.grid(row=0, column=1)

    ajouter_bt = tkinter.Button(fenetre_gestion, text='Ajouter', command=ouvrir_fenetre_ajouter)
    mdf_bt = tkinter.Button(fenetre_gestion, text='Modifier', command=ouvrir_fenetre_modifier)
    supp_bt = tkinter.Button(fenetre_gestion, text='Supprimer', command=ouvrir_fenetre_suprrimer)
    consult_bt = tkinter.Button(fenetre_gestion, text='Consulter', command=ouvrir_fenetre_consulter)

    #user == fait tout sauf supprimer
    if personne.user_statut == 1:
        ajouter_bt.grid(row=2, column=1)
        mdf_bt.grid(row=3, column=1)
        consult_bt.grid(row=4, column=1)

    #admin == fait tout
    if personne.user_statut == 2:
        ajouter_bt.grid(row=2, column=1)
        mdf_bt.grid(row=3, column=1)
        consult_bt.grid(row=4, column=1)
        supp_bt.grid(row=5, column=1)

    #Client == consulter
    if personne.user_statut == 3:
        consult_bt.grid(row=2, column=1)


def ouvrir_fenetre_ajouter():
    global fenetre_ajouter
    fenetre_ajouter = tkinter.Toplevel(fenetre_gestion)
    fenetre_ajouter.title('Ajouter un evenement')
    fenetre_ajouter.geometry('500x200')
    titre_ajout = tkinter.Label(fenetre_ajouter, text='Ajouter un evenement SVP', width=40)
    titre_ajout.grid(row=0, column=2)
    label_event_num = tkinter.Label(fenetre_ajouter, text='ID : ', width=20)
    label_event_nom = tkinter.Label(fenetre_ajouter, text='Nom  : ', width=20)
    label_event_date_dif = tkinter.Label(fenetre_ajouter, text='Date diffusion : ', width=20)
    label_salla_eve = tkinter.Label(fenetre_ajouter, text='Salle_evenement : ', width=20)
    label_event_nb_places_reservees = tkinter.Label(fenetre_ajouter, text='Nombre de places à reserver : ', width=20)
    evenement.num = tkinter.StringVar()
    evenement.nom = tkinter.StringVar()
    evenement.date_dif = tkinter.StringVar()
    evenement.salle_eve = tkinter.StringVar()
    evenement.nb_palces_reserevees = tkinter.StringVar()
    e_num = tkinter.Entry(fenetre_ajouter, width=30, textvariable=evenement.num)
    e_nom = tkinter.Entry(fenetre_ajouter, width=30, textvariable=evenement.nom)
    e_date_dif = tkinter.Entry(fenetre_ajouter, width=30, textvariable=evenement.date_dif)
    e_salle_eve = tkinter.Entry(fenetre_ajouter, width=30, textvariable=evenement.salle_eve)
    e_nb_places_reservees = tkinter.Entry(fenetre_ajouter, width=30, textvariable=evenement.nb_palces_reserevees)
    label_event_num.grid(row=1, column=1)
    label_event_nom.grid(row=2, column=1)
    label_event_date_dif.grid(row=3, column=1)
    label_salla_eve.grid(row=4, column=1)
    label_event_nb_places_reservees.grid(row=5, column=1)
    e_num.grid(row=1, column=2)
    e_nom.grid(row=2, column=2)
    e_date_dif.grid(row=3, column=2)
    e_salle_eve.grid(row=4, column=2)
    e_nb_places_reservees.grid(row=5, column=2)
    ajout_bt = tkinter.Button(fenetre_ajouter, text='Ajouter', command=envoyer_aufichier)
    ajout_bt.grid(row=7, column=4)


def envoyer_aufichier():
    ev_num = evenement.num.get()
    ev_nom = evenement.nom.get()
    ev_date_dif = evenement.date_dif.get()
    ev_salle_eve = evenement.salle_eve.get()
    ev_nb_palces_reserevees = evenement.nb_palces_reserevees.get()
    with open('event.csv', 'a', newline='') as fichiercsv:
        writer = csv.writer(fichiercsv)
        writer.writerow([ev_num, ev_nom, ev_date_dif, ev_salle_eve, ev_nb_palces_reserevees])
    fenetre_ajouter.destroy()


def ouvrir_fenetre_suprrimer():
    global fenetre_supprimer
    fenetre_supprimer = tkinter.Toplevel(fenetre_gestion)
    fenetre_supprimer.title('Supprimer un evenement')
    fenetre_supprimer.geometry('700x300')
    titre_supp = tkinter.Label(fenetre_supprimer, text='Supprimer l evenement SVP', width=40)
    titre_supp.grid(row=0, column=2)
    label_event_num = tkinter.Label(fenetre_supprimer, text='ID de l eve à supprimer : ', width=30)
    label_event_num.grid(row=1, column=1)
    evenement.num = tkinter.StringVar()
    e_num = tkinter.Entry(fenetre_supprimer, width=30, textvariable=evenement.num)
    e_num.grid(row=1, column=2)
    supp_bt = tkinter.Button(fenetre_supprimer, text='supprimer', command=supprimer_event)
    supp_bt.grid(row=7, column=3)


def supprimer_event():
    ind = 0
    ev_num = evenement.num.get()
    with open('event.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            ind = ind + 1
            if row['id'] == ev_num:
                r = csv.reader(open('event.csv'))
                lines = list(r)
                lines.pop(int(ind))
                writer = csv.writer(open('event.csv', 'w'))
                writer.writerows(lines)
    fenetre_supprimer.destroy()


def ouvrir_fenetre_modifier():
    global fenetre_modifier
    fenetre_modifier = tkinter.Toplevel(fenetre_gestion)
    fenetre_modifier.title('Modifier un evenement')
    fenetre_modifier.geometry('600x200')
    titre_modif = tkinter.Label(fenetre_modifier, text='Modifier l evenement SVP', width=40)
    titre_modif.grid(row=0, column=2)
    label_event_num = tkinter.Label(fenetre_modifier, text='ID de l eve à modifier : ', width=30)
    label_event_nom = tkinter.Label(fenetre_modifier, text='Nom  : ', width=30)
    label_event_date_dif = tkinter.Label(fenetre_modifier, text='Date diffusion : ', width=30)
    label_salla_eve = tkinter.Label(fenetre_modifier, text='Salle_evenement : ', width=30)
    label_event_nb_places_reservees = tkinter.Label(fenetre_modifier, text='Nombre de places à reserver : ', width=30)
    label_event_num.grid(row=1, column=1)
    label_event_nom.grid(row=2, column=1)
    label_event_date_dif.grid(row=3, column=1)
    label_salla_eve.grid(row=4, column=1)
    label_event_nb_places_reservees.grid(row=5, column=1)
    evenement.num = tkinter.StringVar()
    evenement.nom = tkinter.StringVar()
    evenement.date_dif = tkinter.StringVar()
    evenement.salle_eve = tkinter.StringVar()
    evenement.nb_palces_reserevees = tkinter.StringVar()
    e_num = tkinter.Entry(fenetre_modifier, width=30, textvariable=evenement.num)
    e_nom = tkinter.Entry(fenetre_modifier, width=30, textvariable=evenement.nom)
    e_date_dif = tkinter.Entry(fenetre_modifier, width=30, textvariable=evenement.date_dif)
    e_salle_eve = tkinter.Entry(fenetre_modifier, width=30, textvariable=evenement.salle_eve)
    e_nb_places_reservees = tkinter.Entry(fenetre_modifier, width=30, textvariable=evenement.nb_palces_reserevees)
    e_num.grid(row=1, column=2)
    e_nom.grid(row=2, column=2)
    e_date_dif.grid(row=3, column=2)
    e_salle_eve.grid(row=4, column=2)
    e_nb_places_reservees.grid(row=5, column=2)
    modifier_bt = tkinter.Button(fenetre_modifier, text='Modifier', command=modifier_event)
    modifier_bt.grid(row=7, column=4)


def modifier_event():
    ind = 0
    with open('event.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        ev_num = evenement.num.get()
        for row in reader:
            ind = ind + 1
            if row['id'] == ev_num:
                ev_nom = evenement.nom.get()
                ev_date_dif = evenement.date_dif.get()
                ev_salle_eve = evenement.salle_eve.get()
                ev_nb_palces_reserevees = evenement.nb_palces_reserevees.get()

                r = csv.reader(open('event.csv'))
                lines = list(r)
                lines[int(ind)][1] = str(ev_nom)
                lines[int(ind)][2] = str(ev_date_dif)
                lines[int(ind)][3] = str(ev_salle_eve)
                lines[int(ind)][4] = str(ev_nb_palces_reserevees)
                writer = csv.writer(open('event.csv', 'w'))
                writer.writerows(lines)

    fenetre_modifier.destroy()


def ouvrir_fenetre_consulter():
    global master
    global variable
    master = tkinter.Toplevel(fenetre_gestion)
    variable = tkinter.StringVar(master)
    variable.set("cette semaine")  # default value
    opt = tkinter.OptionMenu(master, variable, "tout les evenements", "les evenements de cette semaine",
                             "les evenement de ce mois")
    conf = ttk.Button(master, text="Filtrer par date", command=fetch_evenement)
    conf.grid(column=2, row=6, sticky='nwse')
    opt.grid(column=2, row=7, sticky='nwse')


def fetch_evenement():
    master.geometry("1000x1000+300+150")
    master.title("gestion des evenement")
    ind = 2
    has = variable.get()
    mainframe = ttk.Frame(master, padding="2 2 10 10", style='Frame1.TFrame')
    mainframe.grid(column=1, row=3, sticky=(N, W, E, tkinter.S))
    ttk.Label(mainframe, text="Id").grid(column=1, row=1, sticky=W, padx=30)
    ttk.Label(mainframe, text="Nom").grid(column=2, row=1, sticky=W, padx=30)
    ttk.Label(mainframe, text="date de diffusion").grid(column=3, row=1, sticky=W, padx=30)
    ttk.Label(mainframe, text="salle").grid(column=4, row=1, sticky=W, padx=30)
    ttk.Label(mainframe, text="nombre de place ").grid(column=5, row=1, sticky=W, padx=30)
    with open('event.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            jour = row["date_diff"]
            annee = jour[6:10]
            mois = jour[3:5]
            jour = jour[0:2]
            mnt = datetime.datetime.now()
            date_film = datetime.datetime(int(annee), int(mois), int(jour))
            nb_week_mtn = mnt.strftime("%V")
            nb_week_film = date_film.strftime("%V")
            nb_month_mtn = mnt.strftime("%m")
            nb_month_film = date_film.strftime("%m")
            ind = ind + 1
            if has == "tout les evenements":
                ide = row['id']
                nom = row['nom']
                dat = row['date_diff']
                salle = row['salle']
                nbr = row['nb_place']
                ttk.Label(mainframe, text=ide).grid(column=1, row=int(ind), sticky=W, padx=20)
                ttk.Label(mainframe, text=nom).grid(column=2, row=int(ind), sticky=W, padx=20)
                ttk.Label(mainframe, text=dat).grid(column=3, row=int(ind), sticky=W, padx=20)
                ttk.Label(mainframe, text=salle).grid(column=4, row=int(ind), sticky=W, padx=20)
                ttk.Label(mainframe, text=nbr).grid(column=5, row=int(ind), sticky=W, padx=20)


            elif has == "les evenement de ce mois":
                if int(nb_month_mtn) == int(nb_month_film):
                    ide1 = row['id']
                    nom1 = row['nom']
                    dat1 = row['date_diff']
                    salle1 = row['salle']
                    nbr1 = row['nb_place']
                    ttk.Label(mainframe, text=ide1).grid(column=1, row=int(ind), sticky=W, padx=20)
                    ttk.Label(mainframe, text=nom1).grid(column=2, row=int(ind), sticky=W, padx=20)
                    ttk.Label(mainframe, text=dat1).grid(column=3, row=int(ind), sticky=W, padx=20)
                    ttk.Label(mainframe, text=salle1).grid(column=4, row=int(ind), sticky=W, padx=20)
                    ttk.Label(mainframe, text=nbr1).grid(column=5, row=int(ind), sticky=W, padx=20)


            elif has == "les evenements de cette semaine":
                if int(nb_week_mtn) == int(nb_week_film):
                    ide2 = row['id']
                    nom2 = row['nom']
                    dat2 = row['date_diff']
                    salle2 = row['salle']
                    nbr2 = row['nb_place']
                    ttk.Label(mainframe, text=ide2).grid(column=1, row=int(ind), sticky=W, padx=20)
                    ttk.Label(mainframe, text=nom2).grid(column=2, row=int(ind), sticky=W, padx=20)
                    ttk.Label(mainframe, text=dat2).grid(column=3, row=int(ind), sticky=W, padx=20)
                    ttk.Label(mainframe, text=salle2).grid(column=4, row=int(ind), sticky=W, padx=20)
                    ttk.Label(mainframe, text=nbr2).grid(column=5, row=int(ind), sticky=W, padx=20)


def fenetre_id():
    global fenetre_identification
    fenetre_identification = tkinter.Tk()
    fenetre_identification.geometry('500x100')
    titre = tkinter.Label(fenetre_identification, text='Identifier vous SVP', width=40)
    label_user_name = tkinter.Label(fenetre_identification, text='Username', width=20)
    label_user_mdp = tkinter.Label(fenetre_identification, text='User mdp', width=20)
    personne.user_name = tkinter.StringVar()
    personne.user_mdp = tkinter.StringVar()
    u_name = tkinter.Entry(fenetre_identification, width=30, textvariable=personne.user_name)
    u_mdp = tkinter.Entry(fenetre_identification, width=30, textvariable=personne.user_mdp)
    titre.grid(row=0, column=2)
    label_user_name.grid(row=1, column=1)
    label_user_mdp.grid(row=2, column=1)
    u_name.grid(row=1, column=2)
    u_mdp.grid(row=2, column=2)
    login_bt = tkinter.Button(fenetre_identification, text='Identifier', command=login)
    login_bt.grid(row=3, column=3)
    fenetre_identification.mainloop()


fenetre_id()
