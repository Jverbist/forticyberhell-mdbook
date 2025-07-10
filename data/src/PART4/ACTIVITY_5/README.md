# Trojan Horse


### LATERAL MOVEMENT

The bloodhound output reveals an interesting group, called **RailwayControl**, with access to a jumpstation.

Our goal is to add a user account into that group, so we can move lateral in the environment and connect to the jumpstation. 

But, to do so, we need permissions in the domain to add a user to that group. How? 

Our enumeration has revealed that Eddie has an account called `eddie.admX` in the `ADMACCOUNTS` group, which is a member of the `Enterprise Admins` group.

You thought EddieX would use the same credentials for his regular user account as for his `Eddie.admX` account?<br>
→ Nope, bad luck!

Maybe we can **fool Eddie in using his ADM credentials in a credential prompt you control**, and obtain his credentials in this way?