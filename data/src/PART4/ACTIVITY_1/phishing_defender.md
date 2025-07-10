# Spearphishing - DEFENDER

**Defender** Congrats, you are promoted to Senior SOC Analyst.
Connect to the Cortex XDR platform to monitor security activities in real time.


<div class=purple>

Continue monitoring the platform throughout the workshop to maintain real-time visibility into malicious activity.
</div>
<br>

<div class=purple>

To log in to the platform, you will need a FIDO2 security key.
</div>

<br>

<div class=red>

To access the Cortex XDR Platform, **you must use the browser on your personal device.** The Virtual Machines within the Cyberhell environment cannot be used, as access requires a FIDO2 Security Key that must be physically connected.
</div>
<br>


### Access the Cortex XDR platform

1. **Login** via the [Cortex-Gateway](https://cyberhell2025.xdr.eu.paloaltonetworks.com/)

    **https://cyberhell2025.xdr.eu.paloaltonetworks.com/**

    ![Panw Cortex](../../images/sliver_palo.png)

1. Click on `Sign in`

    Username: `student+X@nmbs.exn.be` (Where `X` is your student)
    Password is the Cyberhell password.

    <div class="red">

    Make sure to add the `+` symbol, followed by your student-number.
    </div>

    ![Cortex username](../../images/csp_login.png) 

    <div class="red"> 
    
    When prompted for **MFA** click `Security Key`.
    </div>

    ![Cortex QR](../../images/csp_securitykey.png)
    

1. You should be prompted to use a Passkey. <br> **Please ignore that and click on `Use phone, tablet, or security key`**
    
    ![Cortex use key](../../images/csp_fido.png)

    <div class="info">
    DO <b>NOT</b> SCAN THE QR CODE ! Instead, use the FIDO Security Key
    </div>
    <br>

1. Insert the **FIDO2 Security Key** in your computer

    ![Cortex Token](../../images/sliver_cortex_securitytoken.png)

1. **Touch** the FIDO2 Security Key to authenticate.

<br>

---

<br>

**Defender**, as a sysadmin you are working hard and using teams for communication about downtime. Against your better nature you open the file coming in via teams, because after all it comes from a fellow freedom fighter.  

1. Navigate to teams as `EddieX` on your Windows 10 Desktop machine. Inside the teams project you will find the file `“not_so_shady.wsf”` shared to you by `StanX`. 

1. Download and open the file.

    Click the tree dots to Download the file from Teams.

    Open the file on your machine:

    <br>
    <div class="purple">

    **Uncheck** the `Always ask before opening this file` before opening the file
    </div>
    <br>

    ![Phishing open file](../../images/not_so_shady.jpg)


    If it works out, and you can get the file executed by `EddieX`, he will see this on his screen:

    ![Greetings Stan](../../images/phishing_greetings_stan.png)
