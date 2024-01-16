import json
import discord
import os
import time
from discord import option

with open(".creds.json") as data_file:
    data = json.load(data_file)
    discord_bot_token = data["discord_bjarke_token"]
    guild_ids = data['bjarke_guild_ids']

bot = discord.Bot()

sounds_dict = {
	"HVA SKER DER' ER I GLAR?!": "sfx/misc/glar.mp3",
	"Den skal du kraftedme da have ros for!": "sfx/bjarke/bjarke_denskaldukraftedmedahaverosfor.mp3",
	"I alle sammen": "sfx/bjarke/bjarke_iallesammen.mp3",
	"BJARKE!!!": "sfx/bjarke/bjarke.mp3",
	"Må jeg godt spørge om en ting...": "sfx/bjarke/bjarke_spoergeomenting.mp3",
	"Hvordan kan i blive skudt?!": "sfx/bjarke/bjarke_hvordankanibliveskudt.mp3",
	"Det så godt spillet": "sfx/bjarke/bjarke_amendetsaagodtspillet.mp3",
	"Gør ham da til en Superman": "sfx/bjarke/bjarke_goerhamdatilensupermand.mp3",
	"Bjarke, du skal ikke stå der med bomben": "sfx/bjarke/bjarke_duskalikkestaadermedbomben.mp3",
	"Bjarke, du skal med på kort!": "sfx/bjarke/bjarke_duskalmedpaakort.mp3",
	"Nu er Dax ikke der oppe længere...": "sfx/bjarke/bjarke_nuerikkederoppe.mp3",
	"Svend Erik, du må ikk' block!": "sfx/bjarke/bjarke_svenderikdumaaikkblock.mp3",
	"Hvad skal du ud og se på ham os for?": "sfx/bjarke/bjarke_hvadskalduudogsepaahamosfor.mp3",
	"Det kunne vi da ikke?": "sfx/bjarke/bjarke_detkunnevidaikke.mp3",
	"Du kan da se hvordan det gik...": "sfx/bjarke/bjarke_dukandasehvordandetgik.mp3",
	"Hvor er bombe-stedet henne?": "sfx/bjarke/bjarke_hvorvarbombestedethenne.mp3",
	"Hvem kan skyde igennem det hjørne?": "sfx/bjarke/bjarke_skydeigennemdethjoerne.mp3",
	"Sig det til mig!": "sfx/bjarke/bjarke_sigdettilmig.mp3",
	"Jeg vil ha' en demo fra ham": "sfx/bjarke/bjarke_jegvilhaendemofraham.mp3",
	"Hvem var det?": "sfx/bjarke/bjarke_hvemvardet.mp3",
	"Bjarke, hvem var det?!": "sfx/bjarke/bjarke_hvemvardet2.mp3",
	"Få nu syltet ham!": "sfx/bjarke/bjarke_faanusyltetham.mp3",
	"Jeg skyder dig...": "sfx/bjarke/bjarke_jegskyderdig.mp3",
	"Du har 18 sekunder, løb dit svin...": "sfx/bjarke/bjarke_duhar18sekunder.mp3",
	"Kom ind og få plantet den bombe": "sfx/bjarke/bjarke_komindogfaaplantetdenbombe.mp3",
	"Plant!": "sfx/bjarke/bjarke_plant.mp3",
	"Storm B, storm B...": "sfx/bjarke/bjarke_kombstormb.mp3",
	"Det kan ikke diskuteres...": "sfx/bjarke/bjarke_denkanikkediskuteres.mp3",
	"Prøv nu og hør her...": "sfx/bjarke/bjarke_prvoenuoghoerher.mp3",
	"Team træls pis": "sfx/bjarke/bjarke_teamtraelspis.mp3",
	"Fatter bare lidt...": "sfx/bjarke/bjarke_fatterbarelidt.mp3",
	"Jeg har sagt til ham 20 gange...": "sfx/bjarke/bjarke_sagttilham20gange.mp3",
	"Ham der han skyder lige 3 af vores...": "sfx/bjarke/bjarke_hanskyderlige3afvores.mp3",
	"Det når du nok heller ikke": "sfx/bjarke/bjarke_detnaardunokhellerikke.mp3",
	"Ej ved du hva' mand...": "sfx/bjarke/bjarke_ejholdkaeftman.mp3",
	"Find dig sku' da en anden hobby": "sfx/bjarke/bjarke_finddigskudaenandenhobby.mp3",
	"Kort, kort, kort, kort!!": "sfx/bjarke/bjarke_kortkortkort.mp3",
	"Flygt": "sfx/bjarke/bjarke_flygt.mp3",
	"Prøv nu lige og hold kæft": "sfx/bjarke/wow/bjarke_proevnuligeogholdkaeft.mp3",
	"Hvad er det der er farligt?": "sfx/bjarke/wow/bjarke_hvaderdetderfarligt.mp3",
	"Må jeg høre?": "sfx/bjarke/wow/bjarke_maajeghoere.mp3",
	"Hvorfor?": "sfx/bjarke/wow/bjarke_hvorfor.mp3",
	"Det jo ikke et svar, vel.": "sfx/bjarke/wow/bjarke_detjoikkeetsvarvel.mp3",
	"Hvorfor bekymrer du dig så meget...": "sfx/bjarke/wow/bjarke_hvorforbekymrerdudigomdetotems.mp3",
	"Der er faktisk kun én totem der er...": "sfx/bjarke/wow/bjarke_dererfaktiskkunentotemderertraels.mp3",
	"Det en grounding totem, første gang...": "sfx/bjarke/wow/bjarke_detengroundingtotem.mp3",
	"Og hva' så?!": "sfx/bjarke/wow/bjarke_oghvasaa.mp3",
	"Der er ikke en hvor der står rogue kan...": "sfx/bjarke/wow/bjarke_dererikkeenhvorderstaarrogue.mp3",
	"Kan han hamre igennem på...": "sfx/bjarke/wow/bjarke_kanhanhamreigennempaa.mp3",
	"Hold nu kæft man...": "sfx/bjarke/wow/bjarke_holdnukaeftman.mp3",
	"Du skal ikke snakke om farver...": "sfx/bjarke/wow/bjarke_duskalikkesnakkeomfarver.mp3",
	"Farven har et navn": "sfx/bjarke/wow/bjarke_farvenharetnavn.mp3",
	"Hvad er en grounding totem...": "sfx/bjarke/wow/bjarke_hvaderengroundingtotem.mp3",
	"Tror jeg ikke": "sfx/bjarke/wow/bjarke_trorjegikke.mp3",
	"Hvorfor bliver du ikke roguen med...": "sfx/bjarke/wow/bjarke_hvorforblinderduikkeroguen.mp3",
	"Jeg skal vide hvorfor du ikke gør det": "sfx/bjarke/wow/bjarke_jegskalvidehvorforduikkegoerdet.mp3",
	"Det mig en kæmpe gåde!": "sfx/bjarke/wow/bjarke_detmigenkaempegaade.mp3",
	"Du ved vi skal slå Shamaanen ihjel...": "sfx/bjarke/wow/bjarke_duvedviskalslaa.mp3",
	"Hva' ?": "sfx/bjarke/wow/bjarke_hva.mp3",
	"Der er en level 68 der søger...": "sfx/bjarke/wow/bjarke_dererenlevel68dersoeger.mp3",
	"Så kan hun fortælle dig hvad spillet...": "sfx/bjarke/wow/bjarke_saakanhunfortaelledighvadspillet.mp3",
	"Så kan din kæreste spille den": "sfx/bjarke/wow/bjarke_saakandinkaerstespilleden.mp3",
	"Hun skal have rimelig lang tid til at...": "sfx/bjarke/wow/bjarke_hunskalhaverimeliglangtid.mp3",
	"Du skulle ikke igennem noget!": "sfx/bjarke/wow/duskulleikkeigennemnoget.mp3",
	"Hvordan blinder du?!": "sfx/bjarke/wow/hvordanblinderdu.mp3",
	"Hvordan gør du det?": "sfx/bjarke/wow/hvordangoerdudet.mp3",
	"Så skal du trykke to gange på tab!": "sfx/bjarke/wow/saaskaldutrykketogangepaatab.mp3",
	"Eller hvad fanden du skal tryk....hvad?!": "sfx/bjarke/wow/ellerhvafandenduskaltrykkehvad.mp3",
	"Hva' siger du? Hvorfor skal du trykke...": "sfx/bjarke/wow/hvasigerduhvorforskaldutrykkesaamangegange.mp3",
	"Hva' snakker du om": "sfx/bjarke/wow/hvasnakkerduom.mp3",
	"Er du sindsyg?!": "sfx/bjarke/wow/erdusindsyg.mp3",
	"Du har sku' da targetet ham der står...": "sfx/bjarke/wow/duharskudatargetetham.mp3",
	"To gange på hvad": "sfx/bjarke/wow/togangepaahvad.mp3",
	"Forhelvede, jeg bliver sindsyg!": "sfx/bjarke/wow/forhelvedejegbliversindsyg.mp3",
	"Hvorfor skal du trykke to gange på tab...": "sfx/bjarke/wow/hvorforskaldutrykketogangepaatab.mp3",
	"Kan du ikke godt bare prøve og spille spillet": "sfx/bjarke/wow/kaduikkebaregodtproeveogspillespillet.mp3",
	"Også tænke dig om": "sfx/bjarke/wow/ogsaataenkedigom.mp3",
	"La' vær med at stå og sig din mor hun har en...": "sfx/bjarke/wow/lavaemedatstaaogsigdinmor.mp3",
	"Jeg har kraftedme et navn, mand!": "sfx/bjarke/wow/jegharkraftedmeetnavnmand.mp3",
	"Kom nu ud og find ud af hvor der er nogen henne": "sfx/bjarke/wow/komnuudogfindudafhvorderernogenhenne.mp3",
	"Jamen.. få ham nu slået ihjel!": "sfx/bjarke/wow/jamenfaahamnuslaetihjel.mp3",
	"Jeg gider ikke... jeg kan ikke spille med dig...": "sfx/bjarke/wow/jeggiderikkeduerkraftedmefordummand.mp3",
	"Jeg får kraftedme ondt i maven, mand!": "sfx/bjarke/wow/jegfaarkraftedmeondtimavenmand.mp3",
	"Hvad kan jeg bruge det til om de er grønne...": "sfx/bjarke/wow/hvadkanjegbrugedettil.mp3",
	"Hvorfor kan du ikke bare kigge på dem...": "sfx/bjarke/wow/hvorforkanduikkebarekiggepaadem.mp3",
	"Men det kan jeg da godt se at det er for...": "sfx/bjarke/wow/mendetkanjegdagodtseerformegetforlangt.mp3",
	"Nej, men det os ligemeget!": "sfx/bjarke/wow/nejdetogsaaligemeget.mp3",
	"Ved du hva' mand.. det kraftedme ufatteligt...": "sfx/bjarke/wow/vedduhvamanddeterkraftedmeufatteligt.mp3",
}

async def get_sounds(ctx: discord.AutocompleteContext):
	return sorted([i for i in sounds_dict.keys() if ctx.value.lower() in i.lower()])

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.slash_command(guild_ids=guild_ids, description="Play sound")
async def play(ctx: discord.ApplicationContext, clip: discord.Option(str, "Select a clip", autocomplete=get_sounds)):
    # Tell discord that this might take a bit
    await ctx.defer()
    if ctx.voice_client is None:
        # Check if the user is in a voice channel
        if ctx.author.voice:
            # Connect to the user's voice channel
            voice_channel = ctx.author.voice.channel
            await voice_channel.connect()
        else:
            await ctx.send("You are not connected to a voice channel.")
            return

    sound_path = f"sounds/{sounds_dict[clip]}"

    if not discord.opus.is_loaded():
        discord.opus.load_opus('libopus.so.0')

    if discord.opus.is_loaded() and ctx.voice_client and os.path.exists(sound_path):

        audio_source = discord.FFmpegPCMAudio(sound_path)
        ctx.voice_client.play(audio_source)
        while ctx.voice_client.is_playing():
            time.sleep(1)
        await ctx.voice_client.disconnect()
    await ctx.followup.send(f"Played: {clip}")

bot.run(discord_bot_token)
