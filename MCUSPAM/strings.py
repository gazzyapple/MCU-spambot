from MCUSPAM import CMD_HNDLR as hl

############ TEXTS ############ 
# Error handling text
count_e_text = "Count must be a number(integer > 1) 😇"
delay_e_text = "Delay must be a number(in secs) 🕐"
bigspam_e_text = f"For bigger spams use {hl}bigspam. 😶‍🌫️"
msg_e_text = "Specify message 😶"
user_e_text = "Specify username 😶" 

# Restrict text
owner_r_text = "Restricted !🚫, This guy is a owner of this bots"
safe_r_text = "Restricted !🚫, This guy is in bot safeguard list"
sudo_r_text = "Restricted !🚫, This guy is a sudo user"
safeg_r_text = "Restricted !🚫, This grp is in bot safeguard list"

#Activated/Decativated Status
replyraid_a_text = "Replyraid Activated  ✅"
replyraid_d_text = "Replyraid Deactivated"
echo_a_text = "Echo Activated On The User ✅"
echo_d_text = "Echo Has Been Stopped For The User"
echo_aa_text = "Echo Is Already Activated On This User ✅!!"
echo_ad_text = "Echo Is Already Disabled !!"
replyraid_ad_text = "Replyraid Already Deactivated"

#leave/Join 
join_text = "𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐉𝐨𝐢𝐧𝐞𝐝 𝐓𝐡𝐞 𝐂𝐡𝐚𝐭 ✅"
left_text = "𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐋𝐞𝐟𝐭 𝐓𝐡𝐞 𝐂𝐡𝐚𝐭 ✅"


############ MODULE and USAGE ############ 
module_s = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 : 𝗦𝗽𝗮𝗺 \nCommand:\n"
usage_s = {}
module_r = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 : 𝗥𝗮𝗶𝗱 \nCommand:\n"
usage_r = {}
module_e = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 : 𝗘𝗰𝗵𝗼 \nCommand:\n"
usage_e = {}
module_l = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 : 𝗟𝗲𝗮𝘃𝗲 \nCommand:\n"
usage_l = {} 

usage_s['spam'] = f"`{hl}spam` <count> <message to spam>\n`{hl}spam` <count> <reply to a message>\n\nCount must be a integer"
usage_s['nspam'] = f"`{hl}nspam` <count> (select `n` prefix => `h` for hug🤗, `s` for slap🤚, `d` for dance🕺)"
usage_s['bigspam'] = f"`{hl}bigspam` <count> <message to spam>\n`{hl}bigspam` <count> <reply to a message>\n\nCount must be a integer."
usage_s['delayspam'] = f"`{hl}delayspam` <delay (in sec)> <count> <message to spam>\n`{hl}delayspam` <delay (in sec)> <count> <reply to a message>\n\nCount and delay must be integers"     

usage_r['nraid'] = f"`{hl}nraid` <count> <Username of User>\n`{hl}nraid` <count> <reply to a User>\n (select `n` prefix => `e` for emoji😀, `f` for flirtlines🌚, `v` for quotes😇,`b` for birthday wishes!🎂)\n\nCount must be a integer"
usage_r['replyraid'] = f"`{hl}replyraid` <Username of User>\n`{hl}replyraid` <reply to a User>."
usage_r['dreplyraid'] = f"`{hl}dreplyraid` <Username of User>\n`{hl}dreplyraid` <reply to a User>"
usage_r['delayraid'] = f"`{hl}delayraid` <delay> <count> <Username of User>\n`{hl}delayraid` <delay> <count> <reply to a User>\n\nCount and delay must be integers"         

usage_e['addecho']=f"`{hl}addecho` <reply to a User>"
usage_e['rmecho']=f"`{hl}rmecho` <reply to a User>"

usage_l['join'] = f"`{hl}join` <Chat username or Chat ID>"
usage_l['leave'] = f"`{hl}leave` <Chat username or Chat ID>"

usage = [usage_s,usage_r,usage_e,usage_l]
module = [module_s,module_r,module_e,module_l]
