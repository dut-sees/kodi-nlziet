import os, xbmcaddon, xbmcvfs

ADDON = xbmcaddon.Addon()
ADDON_FANART = ADDON.getAddonInfo('fanart')
ADDON_ID = ADDON.getAddonInfo('id')
ADDON_ICON = ADDON.getAddonInfo('icon')
ADDON_NAME = ADDON.getAddonInfo('name')
ADDON_PATH = xbmcvfs.translatePath(ADDON.getAddonInfo('path'))
ADDON_PROFILE = xbmcvfs.translatePath(ADDON.getAddonInfo('profile'))
ADDON_VERSION = ADDON.getAddonInfo('version')

PROVIDER_NAME = ADDON_ID.replace('plugin.video.', '')

CONST_DUT_EPG_BASE = 'https://dut-epg.github.io'
CONST_DUT_EPG = '{base_epg}/{provider}'.format(base_epg=CONST_DUT_EPG_BASE, provider=PROVIDER_NAME)

try:
    CONST_DUT_EPG_SETTINGS = '{base_epg}/{letter}.settings.json'.format(base_epg=CONST_DUT_EPG_BASE, letter=PROVIDER_NAME[0])
except:
    CONST_DUT_EPG_SETTINGS = '{base_epg}/a.settings.json'.format(base_epg=CONST_DUT_EPG_BASE)

ADDONS_PATH = os.path.join(xbmcvfs.translatePath('special://home'), 'addons', '')
USERDATA_PATH = os.path.join(xbmcvfs.translatePath('special://userdata'), '')

AUDIO_LANGUAGES = {
    'nl': 'Nederlands/Dutch',
    'en': 'Engels/English',
    'gos': 'Gesproken ondertiteling/Spoken subtitles',
    'unk': 'Onbekend/Unknown'
}

LATEST_USER_AGENTS = 'https://jnrbsn.github.io/user-agents/user-agents.json'

SESSION_CHUNKSIZE = 4096
