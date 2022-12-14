from MCUSPAM import CMD_HNDLR as hl

############ TEXTS ############ 
# Error handling text
count_e_text = "Count must be a number(integer > 1) ๐"
delay_e_text = "Delay must be a number(in secs) ๐"
bigspam_e_text = f"For bigger spams use {hl}bigspam. ๐ถโ๐ซ๏ธ"
msg_e_text = "Specify message ๐ถ"
user_e_text = "Specify username ๐ถ" 

# Restrict text
owner_r_text = "Restricted !๐ซ, This guy is a owner of this bots"
safe_r_text = "Restricted !๐ซ, This guy is in bot safeguard list"
sudo_r_text = "Restricted !๐ซ, This guy is a sudo user"
safeg_r_text = "Restricted !๐ซ, This grp is in bot safeguard list"

#Activated/Decativated Status
replyraid_a_text = "Replyraid Activated  โ"
replyraid_d_text = "Replyraid Deactivated"
echo_a_text = "Echo Activated On The User โ"
echo_d_text = "Echo Has Been Stopped For The User"
echo_aa_text = "Echo Is Already Activated On This User โ!!"
echo_ad_text = "Echo Is Already Disabled !!"
replyraid_ad_text = "Replyraid Already Deactivated"

#leave/Join 
join_text = "๐๐ฎ๐๐๐๐ฌ๐ฌ๐๐ฎ๐ฅ๐ฅ๐ฒ ๐๐จ๐ข๐ง๐๐ ๐๐ก๐ ๐๐ก๐๐ญ โ"
left_text = "๐๐ฎ๐๐๐๐ฌ๐ฌ๐๐ฎ๐ฅ๐ฅ๐ฒ ๐๐๐๐ญ ๐๐ก๐ ๐๐ก๐๐ญ โ"


############ MODULE and USAGE ############ 
module_s = "๐ ๐ผ๐ฑ๐๐น๐ฒ ๐ก๐ฎ๐บ๐ฒ : ๐ฆ๐ฝ๐ฎ๐บ \nCommand:\n"
usage_s = {}
module_r = "๐ ๐ผ๐ฑ๐๐น๐ฒ ๐ก๐ฎ๐บ๐ฒ : ๐ฅ๐ฎ๐ถ๐ฑ \nCommand:\n"
usage_r = {}
module_e = "๐ ๐ผ๐ฑ๐๐น๐ฒ ๐ก๐ฎ๐บ๐ฒ : ๐๐ฐ๐ต๐ผ \nCommand:\n"
usage_e = {}
module_l = "๐ ๐ผ๐ฑ๐๐น๐ฒ ๐ก๐ฎ๐บ๐ฒ : ๐๐ฒ๐ฎ๐๐ฒ \nCommand:\n"
usage_l = {} 

usage_s['spam'] = f"`{hl}spam` <count> <message to spam>\n`{hl}spam` <count> <reply to a message>\n\nCount must be a integer"
usage_s['nspam'] = f"`{hl}nspam` <count> (select `n` prefix => `h` for hug๐ค, `s` for slap๐ค, `d` for dance๐บ)"
usage_s['bigspam'] = f"`{hl}bigspam` <count> <message to spam>\n`{hl}bigspam` <count> <reply to a message>\n\nCount must be a integer."
usage_s['delayspam'] = f"`{hl}delayspam` <delay (in sec)> <count> <message to spam>\n`{hl}delayspam` <delay (in sec)> <count> <reply to a message>\n\nCount and delay must be integers"     

usage_r['nraid'] = f"`{hl}nraid` <count> <Username of User>\n`{hl}nraid` <count> <reply to a User>\n (select `n` prefix => `e` for emoji๐, `f` for flirtlines๐, `v` for quotes๐,`b` for birthday wishes!๐)\n\nCount must be a integer"
usage_r['replyraid'] = f"`{hl}replyraid` <Username of User>\n`{hl}replyraid` <reply to a User>."
usage_r['dreplyraid'] = f"`{hl}dreplyraid` <Username of User>\n`{hl}dreplyraid` <reply to a User>"
usage_r['delayraid'] = f"`{hl}delayraid` <delay> <count> <Username of User>\n`{hl}delayraid` <delay> <count> <reply to a User>\n\nCount and delay must be integers"         

usage_e['addecho']=f"`{hl}addecho` <reply to a User>"
usage_e['rmecho']=f"`{hl}rmecho` <reply to a User>"

usage_l['join'] = f"`{hl}join` <Chat username or Chat ID>"
usage_l['leave'] = f"`{hl}leave` <Chat username or Chat ID>"

usage = [usage_s,usage_r,usage_e,usage_l]
module = [module_s,module_r,module_e,module_l]
