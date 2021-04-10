import streamlit as st
from post import poster1, poster2
import base64
import os
import datetime
#from matplotlib.pyplot import imread
from PIL import Image
import io
import shutil

def main():
    #time
    hour_list = [ str(i) +':00' if j==0 else str(i)+':30' for i in range(1, 12) for j in range(2)]
    hour_list.insert(0, '12:00')
    hour_list.insert(1, '12:30')
   
    st.header('Poster Count Down')
    st.markdown('> Display Count Down in Graphics')

    event_name = st.text_input('Event Name')
    event_backup = st.text_input('Event Backup String')

    st.write('Current Date and Time: ',datetime.datetime.now().strftime('%d-%h-%Y %-I:%M%P'))
    event_date = st.date_input('Event Date', value = None, min_value = None, max_value= None, key = None)
    ev_day = (event_date - datetime.date.today()).days
    if ev_day > 1:
        st.write('Event in ', str(ev_day), 'Days time')
    elif ev_day ==1:
        st.write('Event happenning tomorrow')
    elif ev_day ==0:
        st.write('Event happening today')

    hr = st.checkbox('AM')
    if hr:
        event_time = st.selectbox('Event Time', [i+ ' AM' for i in hour_list])
    else:
        event_time = st.selectbox('Event Time', [i + ' PM' for i in hour_list])
    time = datetime.datetime.strptime(event_time, '%I:%M %p').time()
    dtime = datetime.datetime.combine(event_date, time) - datetime.datetime.now()

    imge = st.file_uploader('Background Image', type= ['jpeg', 'jpg'])
    if imge is not None:
        img_show = Image.open(imge)
        st.image(img_show, width= 300)
    st.info('Select an Image with a wider width!')

    img_contrast = st.selectbox('Image Contrast', ['gray', 'use color'])
    #img_channel = st.selectbox('Image Channel', [None,'green', 'blue', 'red'])
    font_color = st.selectbox('Font Color', ['white', 'black'])


    def get_binary_file_downloader_html(zip_folder = 'posters/poster1', file_label= 'all Images'):
        zip_dir = os.listdir(os.path.join(os.getcwd(), zip_folder))
        if len(zip_dir)  ==1:
            bin_file = os.path.join(os.getcwd(), zip_folder, zip_dir[0]) 
            with open(bin_file, 'rb') as f:
                data = f.read()
            bin_str = base64.b64encode(data).decode()
            href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}"> <input type= "button" value= "Download {file_label}"></a>'
            return href
        else:
            shutil.make_archive('test2', 'zip', zip_folder)
            zip_file = 'test2.zip'
            with open(zip_file, 'rb') as f:
                bytes = f.read()
                b64 = base64.b64encode(bytes).decode()
                href = f"<a href=\'data:file/zip;base64,{b64}\' download='{zip_file}'> <input type= 'button' value= 'Download {file_label}'></a>"
            return href


    #col1, col2, col3, col4, col5 = st.beta_columns(5)
    st.text('\n\n')
    if st.button('Generate Image Timer'):
        #clear poster folder
        for fl in os.listdir(os.path.join(os.getcwd(), 'posters', 'poster1')):
            os.remove(os.path.join(os.getcwd(), 'posters', 'poster1', fl))

        for fl in os.listdir(os.path.join(os.getcwd(), 'posters', 'poster2')):
            os.remove(os.path.join(os.getcwd(), 'posters', 'poster2', fl))
            
        string, backup_string = 'Your Event Name', 'Backup Text'
        #get name, date time and img
        if event_name:
            string = event_name
        else:
            st.error('Enter Event Name!')
        if event_backup:
            backup_string = event_backup
        else:
            st.error('Even Backup Text')

        
        if imge is not None:
            img = imge
        else:
            img = None

        if img_contrast == 'gray':
            img_c = True
        else:
            img_c = False

        dt_days = (event_date - datetime.date.today()).days

        

        if dt_days > 1:
            for i in range(1, dt_days+1):
                if i != 1:
                    stringTime = str(i) + 'Days'
                else:
                    stringTime = str(i) +'Day'
                poster1(string, stringTime, backup_string, i , img, img_c , font_color)
                poster2(string, stringTime, backup_string, i, img, img_c , font_color)
        elif dt_days == 1:
            stringTime = '1Day'
            poster1(string, stringTime, backup_string, 1 , img, img_c , font_color)
            poster2(string, stringTime, backup_string, 1, img, img_c , font_color)
        elif dt_days == 0:
            #in hours or min
            all_secs = dtime.total_seconds()
            thour = int(all_secs // (60*60))
            tmin = int((all_secs / 60) - ((all_secs // (60*60)) * 60))
            tsec = int(all_secs % 60)
            if tmin == 0 and thour > 0:
                if thour == 1:
                    stringTime = f'{thour}Hour'
                else:
                    stringTime = f'{thour}Hours'
                poster1(string, stringTime, backup_string, 1 , img, img_c , font_color)
                poster2(string, stringTime, backup_string, 1, img, img_c , font_color)
            elif tmin > 0 and thour > 0:
                if thour == 1:
                    stringTime = f'{thour}Hr:{tmin}Min'
                else:
                    stringTime = f'{thour}Hrs:{tmin}Min'
                poster1(string, stringTime, backup_string, 1 , img, img_c , font_color)
                poster2(string, stringTime, backup_string, 1, img, img_c , font_color)
            elif thour ==0 and tmin > 0:
                if tmin == 1:
                    stringTime = f'{tmin} Min'
                else:
                    stringTime = f'{tmin} Mins'
                poster1(string, stringTime, backup_string, 1 , img, img_c , font_color)
                poster2(string, stringTime, backup_string, 1, img, img_c , font_color)
            elif thour == 0 and tmin ==0:
                stringTime = f'{tsec} Secs'
                poster1(string, stringTime, backup_string, 1 , img, img_c , font_color)
                poster2(string, stringTime, backup_string, 1, img, img_c , font_color)
            elif thour ==0 and tmin ==0 and tsec ==0:
                stringTime = 'Happening'
            else:
                stringTime = 'Passed'
            
        if stringTime == 'Happenning' or stringTime == 'Passed':
            st.error('Select a future date to make Posters!')
        else:
            #poster1
            st.image(sorted([ os.path.join(os.getcwd(), 'posters', 'poster1', i) for i in os.listdir(os.path.join(os.getcwd(), 'posters', 'poster1'))]), width = 200)
            st.markdown(get_binary_file_downloader_html('posters/poster1', 'all Poster1'), unsafe_allow_html = True)

            #poster2
            st.image(sorted([ os.path.join(os.getcwd(), 'posters', 'poster2', i) for i in os.listdir(os.path.join(os.getcwd(), 'posters', 'poster1'))]), width = 200)
            st.markdown(get_binary_file_downloader_html('posters/poster1', 'all Poster2'), unsafe_allow_html = True)

main()