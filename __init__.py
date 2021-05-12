from adapt.intent import IntentBuilder
from chatterbox import FallbackSkill, intent_handler
from os import mkdir
from os.path import join
class DefaultFallback(FallbackSkill):
    def initialize(self):
        """
            Registers the fallback handler
        """
        self.register_fallback(self.handle_fallback, 10)
        # Any other initialize code you like can be placed here
    def handle_fallback(self, message):

        self.speak('can you repeat Nilsou ?')
        return True
    def shutdown(self):
        """
            Remove this skill from list of fallback skills.
        """
        self.remove_fallback(self.handle_fallback)
        super(DefaultFallback, self).shutdown()
def create_skill():
    return DefaultFallback()