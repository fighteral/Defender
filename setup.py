import cx_Freeze

executables=[cx_Freeze.Executable("defender.py")]
cx_Freeze.setup(
    name="Defender",
    options={"build_exe":{"packages":["pygame"],
                          "include_files":["back1.png","bg2.jpg",
                                           "lazerblu.png","mit.png","regularExplosion00.png",
                                           "regularExplosion01.png","regularExplosion02.png",
                                           "regularExplosion03.png","regularExplosion04.png",
                                           "regularExplosion05.png","regularExplosion06.png",
                                           "regularExplosion07.png","regularExplosion08.png",
                                           "sonicExplosion00.png","sonicExplosion01.png",
                                           "sonicExplosion02.png","sonicExplosion03.png","sonicExplosion04.png",
                                           "sonicExplosion05.png","sonicExplosion06.png","sonicExplosion07.png",
                                           "sonicExplosion08.png","square2.png","xwing.png","shield.png","power.png",
                                           "done.mp3","Explosion1.wav","Explosion2.wav",
                                           "Explosion6.wav","Laser_Shoot7.wav"]}},
    version="1.0",
    description="Shooting Enemy is our passion",
    executables=executables
    )
