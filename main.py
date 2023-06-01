import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class SimpleAppGrid(Widget):
    record_label = ObjectProperty(None)
    record_switch = ObjectProperty(None)
    knee_angle_slider = ObjectProperty(None)

    def record_capture(self):
        if not self.record_switch.active:
            self.record_label.text = 'recording active'
            print(self.record_label.text)
            # self.recording_path = os.path.join(os.getcwd(), 'recordings', str(datetime.datetime.now()).split('.')[0].replace(':', '-').replace(' ', '_') + '_recording.txt')
            # print('recording path: ', self.recording_path)
            # self.frame_array_log = [{} for s in self.source]
        else:
            self.record_label.text = 'recording inactive'
            print(self.record_label.text)
            # if self.recording_path is not None:
            #     save_frame_array_log(self.frame_array_log, self.recording_path)
            #     for i,falog in enumerate(self.frame_array_log):
            #         build_video(
            #             falog,
            #             self.recording_path.replace('.txt', '_'+str(i)+'.avi'),
            #             self.fr,# int(Clock.frames/elapsed_time),
            #         )
            # self.recording_path = None
            # self.frame_array_log = [None for s in self.source]

class SimpleApp(App):
    def build(self):
        return SimpleAppGrid()

if __name__ == '__main__':
    SimpleApp().run()