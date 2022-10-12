import ctypes, sys, random, pyodbc, pyperclip, rsa, base64
from tkinter import *
from hashlib import sha256
import Verify as verify

class Aplication(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master = None)
        self.pack(expand=True, fill="both")
        self.config(background="lightblue")
        
        self.currentuser = ""
        self.nameuser = ''
        
        self.PUBLICKEY = rsa.key.PublicKey(9731112320937030912732003616503951385280975947532250088953141444562324596046512532729205120237157610450773524242643482161373011551136395395944389057925551, 65537)
        self.PRIVATEKEY = rsa.key.PrivateKey(9731112320937030912732003616503951385280975947532250088953141444562324596046512532729205120237157610450773524242643482161373011551136395395944389057925551, 65537, 2346175531121748408564297864479285530903530844362071557372912827342253854183057519581853220333476973351652658882377417212300573117570449010661117992402169, 6362629190851967590158260048039925894735132262570298826015678502823287296826274093, 1529416854109333585286155502099475728682742898882321096369144802511503307)
        
        self.crial0()
        
        self.gotoinicial(first=(True))
        
        dados_conexao = ("Driver={SQL Server};"
                         "Server=DESKTOP-HHC2RUC\SQLEXPRESS;"
                         "Database=geraSenhas;"
        )
        
        self.conexao = pyodbc.connect(dados_conexao)
        self.cursor = self.conexao.cursor()
        
    
    def crial0(self):
        self.linha0 = Frame(self)
        self.linha0.config(background="lightgreen")
        self.linha0.pack(side = 'top', expand = True, fill = 'both')
        
        self.linha01 = Frame(self.linha0)
        self.linha01.config(background="lightgreen")
        self.linha01.pack(side = 'top', expand = True, fill = 'x')
        
            
        
        self.linha02 = Frame(self.linha0)
        self.linha02.config(background="lightblue")
        self.linha02.pack(side = 'bottom', expand = True, fill = 'both')
        
        self.title = Label(self.linha02, bg="lightblue", text="Gerador de Senhas", font="Arial 28")
        self.title.pack( side='top')
        
        self.lberr = Label(self.linha01, text = '')
        self.lberr.pack( side = 'bottom')
        self.lberr.configure(background='lightgreen', foreground='red')
        
        self.button_cadastro = Button(self.linha01, text="Cadastre-se", command=self.cadastro)
        self.button_cadastro.configure(border=10, background="blue")
        self.button_cadastro.pack(side="right", expand=True)
        
        self.button_loga = Button(self.linha01, text="Log in", command=self.login)
        self.button_loga.configure(border=10, background="blue")
        self.button_loga.pack(side="right", expand=True)
        
        self.senha = Entry(self.linha01, show="*")
        self.senha.pack( side = 'right')
        
        self.lbsenha = Label(self.linha01, text = 'Senha:')
        self.lbsenha.pack( side = 'right')
        self.lbsenha.configure(background='lightgreen')
        
        self.usuario = Entry(self.linha01)
        self.usuario.pack( side = 'right')
        
        self.lbusuario = Label(self.linha01, text = 'Usuário:')
        self.lbusuario.pack( side = 'right')
        self.lbusuario.configure(background='lightgreen')
        
    
    def login(self):
        self.lberr.configure(text='')
        use = self.usuario.get()
        shn = self.senha.get()
        
        comando1 = f"""SELECT * FROM Logon WHERE usuario = '{use}'"""
        
        tot = self.cursor.execute(comando1)
        foi = False
        
        for i in tot:
            st = shn + i[3]
            if (sha256(st.encode('ascii')).hexdigest() == i[2]):
                foi = True
                self.currentuser = i[0]
                self.nameuser = i[1]
                break
        
        if not foi:
            self.lberr.configure(text='Usuário ou senha inválidos')
        
        else:
            self.ajeitatop()
    
    def ajeitatop(self):
        self.linha01.destroy()
            
        self.linha01 = Frame(self.linha0)
        self.linha01.config(background="lightgreen")
        self.linha01.pack(side = 'top', expand = True, fill = 'x')
        
        self.lberr = Label(self.linha01, text = '')
        self.lberr.pack( side = 'bottom')
        self.lberr.configure(background='lightgreen', foreground='red')
        
        self.button_logout = Button(self.linha01, text="Log out", command=self.logout)
        self.button_logout.configure(border=10, background="blue")
        self.button_logout.pack(side="right")
        
        self.lblogeduser = Label(self.linha01, text = ('Bem Vindo, ' + self.nameuser))
        self.lblogeduser.pack( side = 'right')
        self.lblogeduser.configure(background='lightgreen')
    
    def logout(self):
        self.currentuser =  ''
        self.nameuser = ''
        self.linha0.destroy()
        self.input.destroy()
        self.crial0()
        self.gotoinicial(first=(True))
        
    
    def cadastro(self):
        self.isAdmin()
        self.lberr.config(text='')
        self.linha0.destroy()
        self.input.destroy()
        
        self.crial0()
        
        self.input = Frame(master=self)
        self.input.config(background="lightblue")
        self.input.pack(side = 'top', expand = True, fill = 'both')
        
        self.linha1 = Frame(self.input)
        self.linha1.config(background="lightblue")
        self.linha1.pack(side = 'top', expand = True, fill = 'x')
        
        self.linha2 = Frame(self.input)
        self.linha2.config(background="lightblue")
        self.linha2.pack(side = 'top', expand = True, fill = 'x')
        
        self.linha3 = Frame(self.input)
        self.linha3.config(background="lightblue")
        self.linha3.pack(side = 'top', expand = True, fill = 'x')
        
        self.linha4 = Frame(self.input)
        self.linha4.config(background="lightblue")
        self.linha4.pack(side = 'top', expand = True, fill = 'x')
        
        self.lbusuario = Label(self.linha1, text = 'Usuário:')
        self.lbusuario.pack( side = 'left')
        self.lbusuario.configure(background='lightgreen')
        
        self.criausuario = Entry(self.linha1)
        self.criausuario.focus()
        self.criausuario.pack( side = 'left')
        
        self.lbcriasenha = Label(self.linha2, text = 'Senha:')
        self.lbcriasenha.pack( side = 'left')
        self.lbcriasenha.configure(background='lightgreen')
        
        self.criasenha = Entry(self.linha2, show="*")
        self.criasenha.pack( side = 'left')
        
        self.lbconfirmasenha = Label(self.linha3, text = 'Confirme sua Senha:')
        self.lbconfirmasenha.pack( side = 'left')
        self.lbconfirmasenha.configure(background='lightgreen')
        
        self.confirmasenha = Entry(self.linha3, show="*")
        self.confirmasenha.pack( side = 'left')
        
        self.button_efetuacadastro = Button(self.linha4, text="Efetuar cadastro", command=self.efetuacadastro)
        self.button_efetuacadastro.configure(border=10, background="blue")
        self.button_efetuacadastro.pack(side="top", expand=True, fill = 'x')
        
        self.button_volta = Button(self.linha4, text="Voltar", command=self.gotoinicial)
        self.button_volta.configure(border=10, background="blue")
        self.button_volta.pack(side="top", expand=True, fill='x')
    
    def efetuacadastro(self):
        
        
        user = self.criausuario.get()
        
        if self.criasenha.get() == self.confirmasenha.get():
            sal = self.geraPassword(n = 12, prohibitedstring="""<"'`´>""")
            salted = self.criasenha.get() + sal
            
            hsh = sha256(salted.encode('ascii')).hexdigest()
        
        comando = f"""INSERT INTO Logon(usuario, senha, sal) VALUES 
        ('{user}', '{hsh}', '{sal}')"""
        
        self.cursor.execute(comando)
        self.cursor.commit()
        
        self.gotoinicial()
        
    
    def retrive(self):
        if not self.currentuser:
            self.lberr.config(text="Você precisa estar logado para acessar essa página.")
        else:
            if not self.isAdmin():
                self.lberr.config(text="Você precisa ser o administrador para prosseguir.")
            else:
                self.linha0.destroy()
                self.input.destroy()
                
                comando = """SELECT * from Passwords WHERE userid = ?"""
                
                tot = self.cursor.execute(comando, (self.currentuser))
                
                self.linha0 = Frame(self)
                self.linha0.config(background="lightgreen")
                self.linha0.grid(row = 0)
                
                
                self.button_logout = Button(self.linha0, text="Log out", command=self.logout)
                self.button_logout.configure(border=10, background="blue")
                self.button_logout.grid(column = 2, row = 0)
                j = 0
                for i in tot:
                    j += 1
                    lbdes = Label(self.linha0, text = (i[1]))
                    lbdes.grid(column = 0, row = j)
                    
                    # teste12 = b'FwOnva1AFsWFA2SN4ti5YU2OAlmfPomo2ENoeg2NxNGcxBNVJbqTOeQffzhFRVx9agj8tMtB3RFz5GdnsM4R9g=='
                    # print(bytes(i[2], 'ascii')[2:-1])
                    # print(teste12)
                    # print(teste12 == bytes(i[2], 'ascii')[2:-1])
                    
                    lbpass = Label(self.linha0, text = (self.decrypt(bytes(i[2], 'ascii')[2:-1])))
                    lbpass.grid(column = 1, row = j)
                    
                    bt_copy = Button(self.linha0, text="Copiar",  command= lambda: self.copy(self.decrypt(bytes(i[2], 'ascii')[2:-1])))
                    bt_copy.configure(border=10)
                    bt_copy.grid(column = 2, row = j)
                    
    
    def decrypt(self, string):        
        ans = base64.b64decode(string)
        
        decstring = rsa.decrypt(ans, self.PRIVATEKEY).decode()
        
        return decstring
    
    def encrypt(self, string):        
        encstring = rsa.encrypt(string.encode(), self.PUBLICKEY)
        
        ans = base64.b64encode(encstring)
        
        ans2 = base64.b64decode(ans)
        print(ans2==encstring)
        
        return ans
    

    def gotoinicial(self, first = False):
        if not self.currentuser:
            self.linha0.destroy()
            self.crial0()
            
        if not first:
            self.input.destroy()
        
        self.input = Frame(master=self)
        self.input.config(background="lightblue")
        self.input.pack(side = 'top', expand = True, fill = 'both')
        
        self.linha1 = Frame(self.input)
        self.linha1.config(background="lightblue")
        self.linha1.pack(side = 'top', expand = True, fill = 'x')
        
        self.linha2 = Frame(self.input)
        self.linha2.config(background="lightblue")
        self.linha2.pack(side = 'top', expand = True, fill = 'x')
        
        subtitle = Label(self.linha1, bg="lightblue", text = "Bem vindo ao gerador de senhas fortes, \n o que deseja?", font="Arial 20")
        subtitle.pack(side = 'top')
        
        gotomain = Button(self.linha2, text="Quero gerar senhas", command=self.mainpage)
        gotomain.configure(border=10, background="blue")
        gotomain.pack(side="left", expand=True, fill='x')
        
        gotoretrive = Button(self.linha2, text="Quero recuperar minhas senhas", command=self.retrive)
        gotoretrive.configure(border=10, background="blue")
        gotoretrive.pack(side="left", expand=True, fill='x')
    
    def mainpage(self):
        
        self.input.destroy()
        self.has_copy = False
        
        self.input = Frame(master=self)
        self.input.config(background="lightblue")
        self.input.pack(side = 'top', expand = True, fill = 'both')
        
        self.linha1 = Frame(self.input)
        self.linha1.config(background="lightblue")
        self.linha1.pack(side = 'top', expand = True, fill = 'x')
        
        self.linha2 = Frame(self.input)
        self.linha2.config(background="lightblue")
        self.linha2.pack(side = 'top', expand = True, fill = 'x')
        
        self.linha3 = Frame(self.input)
        self.linha3.config(background="lightblue")
        self.linha3.pack(side = 'top', expand = True, fill = 'x')
        
        self.linha351 = Frame(self.linha3)
        self.linha351.config(background="lightblue")
        self.linha351.pack(side = 'left', expand = True, fill = 'y')
        
        self.linha352 = Frame(self.linha3)
        self.linha352.config(background="lightblue")
        self.linha352.pack(side = 'right', expand = True, fill = 'both')
        
        self.linha4 = Frame(self.input)
        self.linha4.config(background="lightgreen")
        self.linha4.pack(side = 'bottom', expand = True, fill = 'x')
        
        self.lb1 = Label(self.linha1, text = 'Quantidade de digitos (default 8):')
        self.lb1.pack( side = 'left')
        self.lb1.configure(background='lightblue')
        
        self.digitos = Entry(self.linha1, font="Arial 12")
        self.digitos.pack( side = 'left')
        
        self.lb2 = Label(self.linha2, text = 'Caracteres proibidos na senha: ')
        self.lb2.pack( side = 'left')
        self.lb2.configure(background='lightblue')
        
        self.prohibitedstring = Entry(self.linha2, font="Arial 12")
        self.prohibitedstring.pack( side = 'left')
        
        self.upvar = IntVar(self);
        
        self.up = Checkbutton (self.linha351, text="Não incluir letras maiúsculas", var = self.upvar)
        self.up.config(background= "lightgray")
        self.up.pack(side='top')
        
        self.lowervar = IntVar(self);
        
        self.lower = Checkbutton (self.linha351, text="Não incluir letras minúsculas", var = self.lowervar)
        self.lower.config(background= "lightgray")
        self.lower.pack(side='top')
        
        self.especialvar = IntVar(self)
        
        self.especial = Checkbutton (self.linha351, text="Não incluir caracteres especiais", var = self.especialvar)
        self.especial.config(background= "lightgray")
        self.especial.pack(side='top')
        
        self.numbervar = IntVar(self)
        
        self.number = Checkbutton (self.linha351, text="Não incluir números", var = self.numbervar)
        self.number.config(background= "lightgray")
        self.number.pack(side='top')
        
        self.button_gera = Button(self.linha4, text="Gerar senha", command=self.gera)
        self.button_gera.configure(border=10, background="blue")
        self.button_gera.pack(side="top", expand=True, fill='x')
        
        self.button_volta = Button(self.linha4, text="Voltar", command=self.gotoinicial)
        self.button_volta.configure(border=10, background="blue")
        self.button_volta.pack(side="top", expand=True, fill='x')
        
        self.lbpass = Label(self.linha4, text = '', font= "Arial 16")
        self.lbpass.pack( side = 'bottom', expand = True, fill = 'x')
        self.lbpass.configure(background='lightgreen')
    
    def save(self, password):
        if not self.currentuser:
            self.lberr.config(text="Você precisa estar logado para prosseguir.")
        else:
            if not self.isAdmin():
                self.lberr.config(text="Você precisa ser o administrador para prosseguir.")
            else:
                desc = simpledialog.askstring("Input", "Descrição da senha: ", parent = self.input)
                encpass = self.encrypt(password)
                
                comando = """INSERT INTO Passwords (description, password, userid) 
                VALUES (?, ?, ?)"""
                self.cursor.execute(comando, (desc, str(encpass) , int(self.currentuser)))
                self.cursor.commit()
                try:
                    
                
                    messagebox.showinfo("Information", "Sua senha foi salva com sucesso.")
                except:
                    messagebox.showerror("Error", "Não foi possivel salvar sua senha, tente novamente mais tarde.")
                
    def gera(self):
        self.lberr.config(text="")
        self.lbpass.config(text = "")
        if self.upvar.get() == 0:
            upvar1 = True
        else:
            upvar1 = False
            
        if self.lowervar.get() == 0:
            lowervar1 = True
        else:
            lowervar1 = False
            
        if self.especialvar.get() == 0:
            especialvar1 = True
        else:
            especialvar1 = False
            
        if self.numbervar.get() == 0:
            numbervar1 = True
        else:
            numbervar1 = False
        
        if self.digitos.get():
            try:
                n = int(self.digitos.get())
            except:
                n = 8
                self.lberr.config(text="Erro, o campo de numero de dígitos deve ser preenchido com números, valor default é 8")
        else:
            n = 8
        proibido = ""
        
        if self.prohibitedstring.get():
            proibido = self.prohibitedstring.get()
        
        password = self.geraPassword(n, especial =especialvar1, number = numbervar1, lower=lowervar1, up = upvar1, prohibitedstring=proibido)
        
        if password == -1:
            self.lbpass.config(text = " Impossível gerar uma senha com os requisitos solicitados")
        else:
            self.lbpass.config(text = " Sua senha é: \n" + password )
            if (not self.has_copy):
                
                self.button_save = Button(self.linha4, text="Salvar senha", command= lambda: self.save(password))
                self.button_save.configure(border=10, background="blue")
                self.button_save.pack(side="left", expand=True, fill='x')
                
                self.button_copy = Button(self.linha4, text="Copiar para area de transferencia",  command= lambda: self.copy(password))
                self.button_copy.configure(border=10, background="blue")
                self.button_copy.pack(side="right", expand=True, fill ='x' )
                self.has_copy = True
     
    def copy(self, password):
        pyperclip.copy(password)
    
    def isAdmin(self):
        verify.verificaAdmin()
        return True
        # else:
        #     return False
        # try:
        #     return ctypes.windll.shell32.isUserAdmin()
        # except:
                
        #     ret = ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None)
            
        #     if(int(ret) <= 32):
        #         return False
        #     else:
        #         return True
    
    def geraPassword(self, n = 8, especial = True, number = True, lower = True, up = True, prohibitedstring = ""):
        hasUp = False
        hasLower = False
        hasEspecial = False
        hasNumber = False
        escape = 0
        prohibited = []
        
    
        for j in prohibitedstring:
            prohibited.append(j)
        
        if (type(n) == int or type(n) == float):
            n = int(n)
        else:
            return -1
        
        if n < (int(especial) + int(number) + int(lower) + int(up)):
            return -1
        
        while ((hasUp != up) or (hasLower != lower) or (hasEspecial != especial) or (hasNumber != number)):
            hasUp = False
            hasLower = False
            hasEspecial = False
            hasNumber = False
            add = False
            
            password = ""
                
            for i in range(n):
                atual = len(password)
                while( len(password) == atual):
                    let = random.randint(33, 122)
                    
                    if chr(let) not in prohibited:
                        
                        if (let >= 33 and let <= 47 and especial):
                            hasEspecial = True
                            add = True
                        elif (let > 47 and let <= 57 and number):
                            hasNumber = True
                            add = True
                        elif (let > 57 and let <= 64 and especial):
                            hasEspecial = True
                            add = True
                        elif (let > 64 and let <= 90 and up):
                            hasUp = True
                            add = True
                        elif (let > 90 and let <= 96 and especial):
                            hasEspecial = True
                            add = True
                        elif (let > 96 and let <= 122 and lower):
                            hasLower = True
                            add = True
                    else:
                        escape += 1
                    
                    if add:
                        password += chr(let)
                        add = False
                        
                    if escape >= 100000:
                        return -1
        
        return password
    


app = Aplication()
app.master.title("Gerador de Senhas Fortes")
app.master.geometry("500x500")
mainloop()
    