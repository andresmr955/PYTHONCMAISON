def nettoyer_et_inverser_donnees(chaine_fautive):
    print("À FAIRE")
    print(chaine_fautive)
    new_chaine_fautive = chaine_fautive.replace('TMP', '').replace('_', '').replace('&', '-').replace('#', '-')
    

    new_chaine_fautive.strip('TMP')
    list_des_mots = new_chaine_fautive.split('-')
    print(list_des_mots)

    list_des_mots = list_des_mots[0] + '-'+ list_des_mots[2] + '-' + list_des_mots[1]
    print(list_des_mots)

    print(list_des_mots)
    print('new_chaine: ', list_des_mots)

chaine_fautive_1 = "Xn4321_TMP&32°#teMpérature"
chaine_fautive_2 = "Xn4321_TMP&50#huMIDité"


nettoyer_et_inverser_donnees(chaine_fautive_1)
nettoyer_et_inverser_donnees(chaine_fautive_2)
