import kender
import kSoundManager as ksm

person1 = kender.person("kevin", 23)

print(person1.toString())

print(person1.presentate())

# ksm.makeSound( ksm.soundTypes[2] )

ksm.makeSound( "alert" )
