from header import *


# TODO :====================================================
# bomb empliment

# Classes :=================================================
class btn(QPushButton):
    def __init__(self,x,y):
        super().__init__()
        self.value=None
        self.x,self.y=x,y
        self.setText(" ")
        self.setEnabled(True)  # en/desabled
        self.setFixedSize(25,25)
        self.clicked.connect(lambda : window.rec_reveal(self.x,self.y))
        
    
    # def flag:
        
    def SetVal(self,val): 
        print(f"SetVal : ({self.x};{self.y}) = {val}")      
        self.value=val
        
    def GetVal(self):       
        return self.value
        
    def flag(sef): # *flag icon
        pass
    
    def reveal(self): 
        self.setText( str(self.value) )
        self.setEnabled(False)
        if self.value=="*": # *bombe icon
            return "lose"
      
   

        
        
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Vars :==================================================================
        self.FirstMove=1
        self.sizeX,self.sizeY=10,10
        self.sizeBomb = 8
        self.items=[[btn(x,y) for x in range(self.sizeX)] for y in range(self.sizeY)]
        # layouts :================================================================
        # layout 1
        
        # layout 2
        layout2 = QGridLayout()
        layout2.setSpacing(0)
        layout2.setContentsMargins(0,0,0,0)
        
        for x in range(self.sizeX):
            for y in range(self.sizeY):
                layout2.addWidget(self.items[y][x], y+1, x+1)
        
        # layout 3
        MainLayout = QHBoxLayout()
        MainLayout.addLayout(layout2)
        
        widget = QWidget()
        widget.setLayout(MainLayout)
        self.setCentralWidget(widget)
        
    # Functions :==========================================================
    def rec_reveal(self,x=0,y=0):
        print("in rec_rev")
        
        if self.FirstMove:
            print("in rec_rev/firstmove")
            self.FirstMove=0
            self.MakeBombs(x,y)
            self.SetValues()
            print("=================================",x,y)
            # self.revealall()
        print("in rec_rev/end firstmove")
        
        print(x,y)
        if self.items[y][x].text()!=" " :
            print("     rec1")
            return 0
        if self.items[y][x].GetVal()=="*":
            print("     rec2")
            return 0
        elif int(self.items[y][x].GetVal())>0:
            print("     rec3")
            # self.rec_reveal(self.x,self.y)
            self.items[y][x].setText( str(self.items[y][x].GetVal()) )
            self.items[y][x].setEnabled(False)
            return 0
            
        elif self.items[y][x].GetVal()==0 :
            print("     rec3")
            # self.rec_reveal(self.x,self.y)
            self.items[y][x].setText( str(self.items[y][x].GetVal()) )
            self.items[y][x].setEnabled(False)
            if (x+1<self.sizeX): self.rec_reveal(x+1,y)
            if (x-1>=0): self.rec_reveal(x-1,y)
            if (y+1<self.sizeY): self.rec_reveal(x,y+1)
            if (y-1>=0): self.rec_reveal(x,y-1)

            if (x-1>=0 and y-1>=0): self.rec_reveal(x-1,y-1)
            if (x+1<self.sizeX and y+1<self.sizeY): self.rec_reveal(x+1,y+1)
            if (x-1>=0 and y+1<self.sizeY): self.rec_reveal(x-1,y+1)
            if (x+1<self.sizeX and y-1>=0): self.rec_reveal(x+1,y-1)
       
        
    def SetValues(self):    
        for y in range(self.sizeY):
            for x in range(self.sizeX):
                
                if( self.items[y][x].GetVal()=="*"):continue
                count=0
                print(f"#setting value of ({y};{x})")
                if( y>1 and x>1 and self.items[y-1][x-1].GetVal()=="*"):
                    count+=1
                    print(f"     donne {y-1},{x-1}")
                
                 
                if( y>1 and self.items[y-1][x].GetVal()=="*"):
                    count+=1
                    print(f"     donne {y-1},{x}")
                
                 
                if( y>1 and (x+1)<self.sizeX and self.items[y-1][x+1].GetVal()=="*"):
                    count+=1
                    print(f"     donne {y-1},{x+1}")
                
                # =================================================
                 
                if( (y+1)<self.sizeY and x>1 and self.items[y+1][x-1].GetVal()=="*"):
                    count+=1
                    print(f"     donne {y+1},{x-1}")
                
                 
                if( (y+1)<self.sizeY and self.items[y+1][x].GetVal()=="*"):
                    count+=1
                    print(f"     donne {y+1},{x}")
                
                 
                if( (y+1)<self.sizeY and (x+1)<self.sizeX and self.items[y+1][x+1].GetVal()=="*"):
                    count+=1
                    print(f"     donne {y+1},{x+1}")
                
                # =================================================
                 
                if( x>1 and self.items[y][x-1].GetVal()=="*"):
                    count+=1
                    print(f"     donne {y},{x-1}")
                
                
                 
                if( (x+1)<self.sizeX and self.items[y][x+1].GetVal()=="*"):
                    count+=1
                    print(f"     donne {y},{x+1}")
                
                self.items[y][x].SetVal(count)
                

    def MakeBombs(self,x,y):
        c = self.sizeBomb
        while c:     
            tempx,tempy=randint(0,self.sizeX-1),randint(0,self.sizeY-1)
            if(abs(tempy-y)<=1 and abs(tempx-x)<=1): continue
            if self.items[tempy][tempx].value!="*":
                print(f"bomeb[{c}] ({tempy};{tempx})")
                self.items[tempy][tempx].value = "*"
                c-=1
        
    
    def Reset(self):
        for y in range(self.sizeY):
            for x in range(self.sizeX):
                self.items[x][y]=None
                self.items[x][y].setText(" ")
                self.items[x][y].setEnabled(True)
                self.FirstMove = 1
                # reset time
    
    # def revealall(self):
    #     for y in range(self.sizeY):
    #         for x in range(self.sizeX):
    #             self.items[x][y].reveal()         
                  
        
    



# Main :===============================================================

app = QApplication([])

window = MainWindow()

window.show()

app.exec()   
