import sqlite3
# Connexion à la base de données. Si le fichier n'existe pas,il est créé.
# L'objet `conn` représente la connexion à la base de données.
conn = sqlite3.connect('ma_base_de_donnees.db')
# Créer un objet `cursor`. C'est lui qui exécute les commandes SQL.
cursor = conn.cursor()
print("Connexion à la base de données établie avec succès.")

# Requête SQL pour créer une table 'utilisateurs'
cursor.execute('''
CREATE TABLE IF NOT EXISTS utilisateurs (
id INTEGER PRIMARY KEY AUTOINCREMENT,
nom TEXT NOT NULL,
email TEXT UNIQUE NOT NULL
)
''')
# Valider les changements. C'est essentiel pour sauvegarder la table.
conn.commit()
print("Table 'utilisateurs' créée avec succès.")

# Données à insérer
donnees_utilisateur = ('Jean Claude Kabayabaya','jc.kabayabaya@gmail.com')
# Requête d'insertion avec des paramètres de substitution
cursor.execute("INSERT INTO utilisateurs (nom, email) VALUES(?, ?)", donnees_utilisateur)
# Valider l'insertion des données
conn.commit()
print("Utilisateur inséré avec succès.")

utilisateurs = [
('Marie Ciza', 'marie.ciza@gmail.com'),
('Albert Mukunzi', 'albert.mukunzi@gmail.com')
]
cursor.executemany("INSERT INTO utilisateurs (nom, email) VALUES (?, ?)", utilisateurs)
conn.commit()
print("Deux utilisateurs insérés avec succès.")

# Sélectionner tous les utilisateurs
cursor.execute("SELECT id, nom, email FROM utilisateurs")
# Récupérer tous les résultats
resultats = cursor.fetchall()
print("Liste de tous les utilisateurs :")
for utilisateur in resultats:
    print(utilisateur)
# Sélectionner un utilisateur en particulier
nom_recherche = 'Jean Claude Kabayabaya'
cursor.execute("SELECT email FROM utilisateurs WHERE nom=?",
(nom_recherche,))
# Récupérer le premier résultat (ou None si rien n'est trouvé)
email_trouve = cursor.fetchone()
print(f"L'e-mail de {nom_recherche} est : {email_trouve[0]}")

# Mettre à jour l'e-mail de 'Jean Claude Kabayabaya''
nouveau_mail = 'j.claude@yahoo.fr'
nom_a_modifier = 'Jean Claude Kabayabaya'
cursor.execute("UPDATE utilisateurs SET email=? WHERE nom=?",
(nouveau_mail, nom_a_modifier))
conn.commit()
print(f"E-mail de {nom_a_modifier} mis à jour.")
# Supprimer un utilisateur
nom_a_supprimer = 'Marie Ciza'
cursor.execute("DELETE FROM utilisateurs WHERE nom=?",
(nom_a_supprimer,))
conn.commit()
print(f"Utilisateur {nom_a_supprimer} supprimé.")