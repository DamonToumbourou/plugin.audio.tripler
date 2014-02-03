from xbmcswift2 import Plugin, xbmcgui
import tripler

plugin = Plugin()

@plugin.route('/')
def main_menu():
    podcasts = tripler.get_podcasts()
    items = [{
        'label': "Triple R: live stream",
        'path': "http://media.on.net/radio/114.m3u",
        'is_playable': True,
        }]
    return items

#@plugin.route('/live_stream')



if __name__ == '__main__':
    plugin.run()