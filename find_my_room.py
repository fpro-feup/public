# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 16:31:54 2021

@author: jlopes

This script finds the room that a student should go to to take an FPRO test, given the students distribution.

You may need to install the 'unidecode' package.
"""

student_dist = { 
  'B101': ("Adam Gershenson Nogueira", "Alexandre Guimaraes Gomes Correia"),
  'B104': ("Alexandre Manuel Luz Rodrigues da Costa", "Duarte Filipe Campos Barbosa Lopes"),
  'B105': ("Eduardo Duarte da Silva", "Francisco Lopes Mendonça"),
  'B201': ("Francisco Miguel Alcobia Maia Prada", "Guilherme Soares Sequeira"),
  'B203': ("Guilherme Valler Moreira", "Igor Liberato de Castro"),
  'B204': ("Igor Rodrigues Diniz", "Joana Inês Gonçalves dos Santos"),
  'B207': ("Joana Vale Amaro de Sousa", "José Marcelino Zacarias Júnior"),
  'B208': ("José Maria Borges Pires do Couto e Castro", "Mariana Mota Azevedo"),
  'B213': ("Mariana Solange Monteiro Rocha", "Pedro Miguel Magalhães Nunes"),
  'B304': ("Pedro Miguel Moreira Ramalho", "Ricardo Filipe Resende Teixeira Pereira"),
  'B305': ("Ricardo Jorge Costa Nogueira", "Sérgio Manuel de Sousa Carvalho e Boura Carvalhais"),
  'B311': ("Simião Jorge Mavie", "Walter Muhanyele Massango") }

from unidecode import unidecode

def name_in(name, left, right):
    return unidecode(left).lower() <= unidecode(name).lower() <= unidecode(right).lower()

name = input("Give me the full Name? ")
room = [k for k, v in student_dist.items() if name_in(name, v[0], v[1])]
if len(room): print(f"In the next assign '{name}' goes to '{room[0]}'!")
