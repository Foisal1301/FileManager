from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

KV = """
ScreenManager:
	FileView:
	ImageView:
	VideoView:

<FileView>
	name:'file'
	BoxLayout:
		orientation:'vertical'
		size:root.width,root.height

		padding: 50
		spacing: 20

		FileChooserListView:
			id:fileChooser
			on_selection: root.selected(fileChooser.selection)

<ImageView>
	name:'image'
	BoxLayout:
		orientation:'vertical'
		size:root.width,root.height

		padding: 50
		spacing: 20

		Button:
			text:'Back'
			on_press:root.manager.current = 'file'
			size_hint: (.2,.02)

		Image:
			id:img
			source:""

<VideoView>
	name:'video'
	BoxLayout:
		orientation:'vertical'
		size:root.width,root.height

		padding: 50
		spacing: 20

		Button:
			text:'Go Back'
			on_press:
				video.state = 'stop'
				root.manager.current = 'file'
			size_hint: (.2,.02)

		VideoPlayer:
			id:video
			source:''
			state: 'play'
			allow_stretch: True
			options:{'eos':'loop'}

"""

class FileView(Screen):
	def selected(self,filename):
		try:
			if filename[0].endswith('.mp4') or filename[0].endswith('.mkv') or filename[0].endswith('.avi'):
				self.manager.current = 'video'
				self.manager.get_screen("video").ids.video.source = filename[0]
			elif filename[0].endswith('.png') or filename[0].endswith('.jpg') or filename[0].endswith('.jpeg'):
				self.manager.current = 'image'
				self.manager.get_screen("image").ids.img.source = filename[0]
		except:
			pass

class ImageView(Screen):
	pass

class VideoView(Screen):
	pass

sm = ScreenManager()
sm.add_widget(FileView(name='file'))
sm.add_widget(ImageView(name='image'))
sm.add_widget(VideoView(name='video'))

class AwesomeApp(App):
	def build(self):
		return Builder.load_string(KV)

if __name__ == '__main__':
	AwesomeApp().run()
