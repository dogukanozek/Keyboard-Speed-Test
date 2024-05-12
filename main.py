from tkinter import *
import customtkinter as ctk
import random
import sys
import os
import subprocess
# Görünümü karanlık modda ayarla
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
word_list = [
    "merhaba", "iyi", "günler", "ev", "okul",
    "kitap", "kalem", "defter", "masa", "sandalye",
    "bilgisayar", "telefon", "çanta", "araba", "bisiklet",
    "kahve", "çay", "su", "yemek", "kahvaltı",
    "öğle", "akşam", "gece", "sabah", "hafta",
    "ay", "yıl", "tatil", "dinlenmek",
    "spor", "müzik", "film", "dizi", "kitaplık",
    "yazar", "şiir", "roman", "hikaye", "sevgi",
    "aşk", "arkadaş", "dost", "aile", "anne",
    "baba", "kardeş", "çocuk", "genç", "yaşlı",
    "saat", "dakika", "saniye", "zaman", "hızlı",
    "yavaş", "renk", "mavi", "yeşil", "kırmızı",
    "sarı", "mor", "turuncu", "güzel", "hoş",
    "mutlu", "üzgün", "korku", "heyecan", "merak",
    "mutluluk", "hüzün", "kıskançlık", "kahkaha", "gözyaşı",
    "özgürlük", "hayat", "umut", "cesaret", "başarı",
    "öğrenmek", "başlamak", "bitirmek", "hayal", "gerçek",
    "özlem", "sessizlik", "rüya", "hediye", "gülümse",
    "gökyüzü", "deniz", "orman", "dağ", "şehir",
    "gezmek", "keşfetmek", "gözlem", "anlamak", "sorgulamak",
    "tebrik", "kutlama", "sevinç", "korku", "şaşkınlık",
    "harika", "inanılmaz", "ilginç", "muhteşem", "sevinmek",
    "heyecanlanmak", "şaşırmak", "dinlenmek", "tatil",
    "tatlı", "acı", "tuzlu", "ekşi", "büyü", "mucize",
    "sevgili", "yalnız", "kalabalık", "sessiz", "gürültülü",
    "yağmur", "kar", "güneş", "rüzgar", "bulut",
    "doğa", "manzara", "şelale", "göl", "nehir",
    "ormanlık", "çiçek", "kuş", "hayvan", "balık",
    "kaplumbağa", "fil", "aslan", "ayı", "zürafa",
    "denizatı", "yıldız", "gezegen", "uzay", "galaksi",
    "kozmik", "parlak", "karanlık", "gizem", "keşif",
    "macera", "serüven", "bilim", "teknoloji", "gelecek"
]
#yazmamız gereken kelimeler için liste



def restart_program():
    root.destroy()
    subprocess.Popen([sys.executable,"main.py"])


def create_result_window(truewordcount=0,falsewordcount=0,total_letter_printing_sum=0):
    
    def on_enter(event):
        restart_button.configure(cursor="hand2")

    result_window=ctk.CTkToplevel()
    my_font = ctk.CTkFont("Century Gothic", 20)
    result_window.title("Sonuçlar")
    result_window.geometry("600x360")

    result_frame1=ctk.CTkFrame(master=result_window,width=400,height=200)
    result_frame1.grid(row=0,column=0,padx=110,pady=20)

    truewordlabel=ctk.CTkLabel(master=result_frame1,text="Doğru Yazılan Kelime Sayısı:",font=my_font)
    truewordlabel.grid(row=0,column=0,padx=20,pady=20)

    truewordlabelcount=ctk.CTkLabel(master=result_frame1,text=truewordcount,font=my_font)
    truewordlabelcount.grid(row=0,column=1,padx=10)

    falsewordlabel=ctk.CTkLabel(master=result_frame1,text="Yanlış Yazılan Kelime Sayısı:",font=my_font)
    falsewordlabel.grid(row=1,column=0,padx=0,pady=20)

    falsewordlabelcount=ctk.CTkLabel(master=result_frame1,text=falsewordcount,font=my_font)
    falsewordlabelcount.grid(row=1,column=1,padx=10)
    
    total_letter_press=ctk.CTkLabel(master=result_frame1,text="Toplam Harf Basımı:",font=my_font)
    total_letter_press.grid(row=2,column=0,padx=20,pady=20)
    
    total_letter_press_sum=ctk.CTkLabel(master=result_frame1,text=total_letter_printing_sum,font=my_font)
    total_letter_press_sum.grid(row=2,column=1,padx=20,pady=20)
    
    restart_button=ctk.CTkButton(master=result_window,text="Restart",font=my_font,command=restart_program)
    restart_button.grid(row=1,column=0,padx=110,pady=20)
    
    restart_button.bind('<Enter>', on_enter)



def entry_change(event):# her entrye harf girildiğinde çalışır

    global i
    global trueword
    global falseword
    global total_letter
    total_letter+=1
    i+=1
    if(i==1):
        start_countdown(1)#sadece bir kere sayac için çalışır 
   
    # Entry widget'ından girilen metni al
    text = user_entry.get()#girilen entryi kontrol eder
    if " " in text:#eğer boşluk tuşuna bastıysa girilen text ile doğru texti karşılaştırır
        is_true=False # girilen text doğruysa true yanlışsa false değerini alır
        if text[0:len(text)-1]==textbox_list[textindex].cget("text"):  # text[0:len(text)-1] olmasının nedeni sonda girdiğimiz boşluk karakterini almamak
            is_true=True 
            trueword+=1 # eğer girilen kelime doğruysa değeri 1 attırıp labela yazdırıyoruz
            written_words_label.configure(text=trueword)
            
        else:
            falseword+=1
            is_true=False
        update_labelframe(textbox_list,is_true)#entry olarak girildikten sonra frame içindeki textleri düzenliyoruz
        user_entry.delete(0,END) # entry kısmınının içeriğini  siliyoruz
        
   
    
   
def start_countdown(minutes):#sürenin çalışması için gereken fonksiyon entrye kısmına bir harf girildiği anda tetiklenir sadece bir defa çalışır
    global remaining_time
    remaining_time = minutes * 60  # Saniye cinsinden kalan süre
    update_countdown()
 
def update_countdown(): #üstteki sayacı başlatan fonksiyonda bir kere çalıştıktan sonra her bir saniye için çalışır
    global remaining_time #kalan süre değişkeni
    if remaining_time > 0:
        minutes = remaining_time // 60
        seconds = remaining_time % 60
        time_str = f"{minutes:02}:{seconds:02}"
        time_label.configure(text=time_str)
        remaining_time -= 1
        # Her saniyede bir zamanlayıcıyı güncelle
        time_label.after(1000, update_countdown)# her bir saniyede bir kere bu fonksiyon çalışır
    else:
        time_label.configure(text="Süre doldu!")
        user_entry.configure(state="disabled")
        create_result_window(trueword,falseword,total_letter)
    

def update_labelframe(textboxlist,is_true):#aşağıdaki fonksiyonda oluşturlan labelları textboxlistesine atıyoruz ve sonra bu fonksiyona parametre olarak yolluyoruz
    global textindex# hangi labelda olduğumuzu bu index ile takip ediyoruz
    is_true=is_true 
    if(textindex==4):#eğer son kelime için entry aldıysak textboxlisti ve framein içeriğini siliyoruz
        textbox_list.clear()
        clear_frame(tabview)
        create_textbox(textboxlist,word_list)#yeni labellerımızı oluşturuyoruz
        textindex=0#en baştaki labela gitmek için textindexi de sıfırlıyoruz
    else:
       if(is_true==True):
            textbox_list[textindex].configure(bg_color="green") # eğer is_true değişkeni true ise yani girilen text ile doğru text aynıysa geçtiğimiz texti yeşil yaparız
            textbox_list[textindex+1].configure(bg_color="blue")
       else:
            textbox_list[textindex].configure(bg_color="red")   # eğer is_true değişkeni true ise yani girilen text ile doğru text aynıysa geçtiğimiz texti kırmızı yaparız
            textbox_list[textindex+1].configure(bg_color="blue")
       textindex+=1 # her boşluk tuşunda yeni labela geçiyoruz
      


def create_textbox(textboxlist,wordlist=None):#labelları oluşturup textboxliste ekleme fonksiyonu
    words=choicetext(wordlist)#labelların içindeki textleri rastgele seçiyoruz
    for j in range(0,5):
        #5 label oluşturuyoruz
        textbox=ctk.CTkLabel(master=tabview,text=words[j],font=ctk.CTkFont("Century Gothic", 17))#
        textbox.grid(row=0,column=j+1,padx=10)
        textboxlist.append(textbox)
        if(j==0):
            #ilk labelın direkt olarak mavi olması için
            textbox.configure(bg_color="blue")

def clear_frame(frame):
    for textbox in frame.winfo_children(): # frame i temizleme fonksiyonu
        textbox.destroy()

def choicetext(wordlist):
    words=list()    # 5 kelime seçip onları listeden çıkarıyoruz
    for a in range(0,5):
       word=random.choice(wordlist)
       words.append(word)
       wordlist.remove(word)
    return words 
    



#Ui part------------------------------------------------------------------------------



# Ana pencereyi oluştur
root = ctk.CTk()
root.title("Klavye Hız Testi")
root.geometry("1080x720")

# Ana başlık etiketi
my_font = ctk.CTkFont("Century Gothic", 40)
main_label = ctk.CTkLabel(master=root, width=1080, text="Klavye Hız Testi", font=my_font, anchor=CENTER)
main_label.grid(row=0, column=0, pady=(0, 10))  # Üst kısmına 10 piksel boşluk bırak

# Frame oluştur ve ana pencereye ekle
frame = ctk.CTkFrame(master=root, bg_color="transparent")
frame.grid(row=2, column=0, pady=70)  # Frame'i alt kısmına 150 piksel boşluk bırak

# Zaman etiketi
time_label = ctk.CTkLabel(master=frame, text="01:00", font=ctk.CTkFont("Century Gothic", 25),anchor=CENTER)
time_label.grid(row=1, column=0, padx=30,pady=5)  # Sol taraftan 20 piksel içeriye yerleştir

# Yazılan kelimeler etiketi
written_words_label = ctk.CTkLabel(master=frame, text="0", font=ctk.CTkFont("Century Gothic", 25),anchor=CENTER)
written_words_label.grid(row=1, column=1, padx=30)  # Sağ taraftan 20 piksel içeriye yerleştir

# 'Kalan Süre' etiketi (ana pencere üzerinde)
top_time_label = ctk.CTkLabel(master=frame, text="Kalan Süre:", font=ctk.CTkFont("Century Gothic", 18))
top_time_label.grid(row=0, column=0,pady=0)  # Alt kısmına yerleştir

written_words_label_top = ctk.CTkLabel(master=frame, text="Doğru Yazılan Kelime Sayısı:", font=ctk.CTkFont("Century Gothic", 18))
written_words_label_top.grid(row=0, column=1,pady=0,padx=15) 


tabview = ctk.CTkFrame(master=root,width=900,height=350)
tabview.grid(row=3,column=0)

user_entry=ctk.CTkEntry(master=root,placeholder_text="kelimeyi giriniz",width=400,height=40,font=ctk.CTkFont("Century Gothic", 16))
user_entry.grid(row=4,column=0,pady=100)

user_entry.bind("<KeyRelease>", entry_change)

#UI part son--------------------------------------------------------------------------------------------------------------------------------



#Programın Çalışması için gereken değişken tanımlamaları


textbox_list=list()#oluşacak labeller için liste oluşturuyoruz


i=0                      #fonksiyonun bir kere çalışması gerekiyor
textindex=0             #labellerı arası geçiş yapmak için textbox_list içindeki indexlere erişiyor
trueword=0              #toplam doğru bilinen kelimeler için
falseword=0 
total_letter=0            #toplam yanlış bilinen kelimeler için
create_textbox(textbox_list,word_list)      #program başlarken ilk kelimeler burada oluşuyor


root.mainloop()#uiın sürekli kalması için
