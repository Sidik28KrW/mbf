B
    ��\�B  �               @   s   d dl Z ee �d�� dS )�    Ns#  �            
   @   sR  �y�d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlmZ	 d dl
mZ dd� Zdd� Zdd	� Zd
d� Zdd� ZdddgZe�  e �d� ed� eed��Zed�Zed�Zeekr�ed� e�  eed��� �� Zedk�r@xPeD ]HZe�d�Z e d  Z!e d Z"ede! d e" d � ee!e"� ee� q�W n�edk�r�x�eD ]JZe�d�Z e d  Z!e d Z"ede! d e" d � ee!e"� ee� �qPW n^edk�r�xReD ]JZe�d�Z e d  Z!e d Z"ede! d e" d � ee!e"� ee� �q�W W nL e#k
�r   ed� Y n0 e$k
�rL Z% zede% � W ddZ%[%X Y nX dS ) �    N)�BeautifulSoup)�LWPCookieJarc        	   &   C   s�  ddkddk } | | > | > |  }dd d g g kddk � | | > | > ddk  || | > | > | | >   || | > | > | | > |  | |     || | > | > | | > |  | |     || | > | > | | > |    || | > | > | | > |  | ddk    | | > | > | | > |  | | > |    | | > | > | | > | |  | ddk    | | > | > | | > | |  | ddk    || | > | > | | > |    || | > | > ddk  || | > | > | | > |  | ddk    || | > | > | | > |  | |     || | > | > | |  ddk   || | > | > |   || | > | > | | > ddk   || | > | > | | > | |  |     | | > | > | | > | |  |    || | > | > | ddk   || | > | > | | > | |  | ddk     || | > | > | | > | |  ddk    | | > | > | | > | |  | ddk    || | > | > | | > |  |    || | > | > ddk  || | > | > | | > |  | |  | ddk     | | > | > | | > | |  | ddk    || | > |  | |    | | > | > | | > |  | ddk   || | > | > | | > |  | | > |     | | > | > | | > |  | | >   || |  |   | | > | > | | > |  | |    || | > |  | |  | ddk    | | > | > | | > |  | ddk   f! }t � � }y�tdd��� }t|�dk�r�td� t�|�}||jk�r�t�	d� td� t
|�|jk�r�t�	d� td� td	t
|� d
 � W n� tk
�r�   y�td�}t|�dk�r$td� t�|�}||jk�r�tdd�}|�|� |��  td� t
|�|jk�r�td� td	t
|� d
 � t�d� ntd� W n" tjjk
�r�   td� Y nX Y n" tjjk
�r�   td� Y nX d S )N� zc%ztoket/.lisensi�r�   z[!!] license invalidz[!!] license invalid :'(z[!!] invalid user :')z[info] send this 'z' to authorz8
[info] contact me: +628887928744 (wa)
[?] license key: �wz[!] license valid :)z[!!] but, invalid user :')g      �?z[err] something else)�platform�open�read�len�exit�requests�get�text�os�remove�str�print�FileNotFoundError�input�write�close�time�sleepZ
exceptionsZRequestException)	�_Z__ZlinkZidosZlisenZreeZinpZreqZliseenr   r   � �lisensi	   sP      � � � � H





r   c             C   sh   t �� at�d� t�d� t�d� dgt_t�d� tjdd� | tj	d< |tj	d< t�
� �� ad S )	NTF)z
User-Agentz#Mozilla/5.0 (Linux; U; Android 5.1)z!https://mbasic.facebook.com/loginr   )�nrZemailZpass)�	mechanizeZBrowser�brZset_handle_equivZset_handle_refererZset_handle_robotsZ
addheadersr	   �select_form�form�submitr
   �res)�mail�pasr   r   r   �login-   s    





r&   c             C   s�  dt t�ksdt t�k�r�t�d|  � tt�� �� dd�}x*|jddd�D ]}d	|d
 krL|d
 }qLW t�|� dtj_	t
�dddd��}t
�|�}tjdd� |d gtjd< t��  dtj_	tjdd� y|d gtjd< W n
   dS t��  dtj_	yrtjdd� |d gtjd< t��  t�� �� }dt |�k�sLdt |�k�r^td|  d � ntd|  d � W n   td� Y nX ntd� d S )Nzsave-device�m_sesszhttps://mbasic.facebook.com/zhtml.parser)�features�aT)�hrefZrapid_reportr*   Zprofile_fake_accountZFRX_PROFILE_REPORT_CONFIRMATIONZyes)�fake�
action_key�checkedr   )r   r+   �tagr,   Fr-   zTerima kasih�Thanksz[+] z success reportedz[-] z failed reportedz[!] already reportedz[!] fail login in to accounts)r   r#   r   r	   �BS�responser
   �find_all�_factory�is_html�json�dumps�loadsr    r!   r"   r   )�id�bs�x�src�js�jso�respr   r   r   �runU;   sF    


r?   c             C   s�  dt t�ksdt t�k�r�t�d|  � tt�� �� dd�}x*|jddd�D ]}d	|d
 krL|d
 }qLW t�|� dtj_	t
�ddddd��}t
�|�}tjdd� |d gtjd< t��  dtj_	tjdd� |d gtjd< t��  dtj_	tjdd� |d gtjd< t��  dtj_	tjdd� yf|d gtjd< t��  t�� �� }dt |�k�sjdt |�k�r|td|  d � ntd|  d � W n   td� Y nX ntd� d S )Nzsave-devicer'   z'https://mbasic.facebook.com/pages/more/zhtml.parser)r(   r)   T)r*   z
/nfx/basicr*   Z	offensiveZ
hatespeechZrace_or_ethnicity�REPORT_CONTENT)�tap1�tap2�tap3r,   r   )r   rA   �answerrB   rC   r,   z%Dikirimkan ke Facebook untuk Ditinjauz Submitted to Facebook for Reviewz[+] z success reportedz[-] z failed reportedz[!] already reportedz[!] fail login in to accounts)r   r#   r   r	   r0   r1   r
   r2   r3   r4   r5   r6   r7   r    r!   r"   r   )r8   r9   r:   r;   r<   r=   r>   r   r   r   �runFe   sJ    


rE   c             C   s@  dt t�ksdt t�k�r4t�d|  d � dtj_ytjdd� W n   tjdd� Y nX dtj_t�d	d
d��}t�	|�}tj
dd� |d gtjd< t��  dtj_tj
dd� yd|d gtjd< t��  t�� �� }dt |�ks�dt |�k�r
td|  d � ntd|  d � W n   td� Y nX ntd� d S )Nzsave-devicer'   z#https://mbasic.facebook.com/groups/z
?view=infoTzLaporkan Grup)r   zReport GroupZpornr@   )�tapr,   r   )r   rF   rD   r,   zTerima kasihr/   z[+] z success reportedz[-] z failed reportedz[!] already reportedz[!] fail login in to accounts)r   r#   r   r	   r3   r4   Zfollow_linkr5   r6   r7   r    r!   r"   r1   r
   r   )r8   r<   r=   r>   r   r   r   �runG�   s6    

rG   Zadlizhafarizadlizhafari.nubZ100024025640715�clearz]
	[ Mass Auto Report ]
	 [ by:KANG-NEWBIE ]
1. report user
2. report pages
3. report groups
	zkang-newbie/> z6
[!] list sparator email|pass
[?] path list accounts: z[?] target id: z[!] fuck you bitchr   �   �|z[!] reported with account [ z ]�   �   z[exit] key interruptzErr: %s)&r   r   �sysr5   r   r   r   Zbs4r   r0   Zhttp.cookiejarr   r   r&   r?   rE   rG   Z	invalidid�systemr   �intr   ZpilZfilr8   r   r	   r
   �
splitlines�filer:   �splitZktlr$   r%   �KeyboardInterrupt�	Exception�Fr   r   r   r   �<module>   s`   8$*,"













  )�marshal�exec�loads� r   r   �+/storage/sdcard1/dcim/coba/Hasil_Mreport.py�<module>   s   