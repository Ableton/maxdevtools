{
    "patcher": {
        "fileversion": 1,
        "appversion": {
            "major": 9,
            "minor": 3,
            "revision": 0,
            "architecture": "x64",
            "modernui": 1
        },
        "classnamespace": "box",
        "rect": [ 67.0, 115.0, 311.0, 320.0 ],
        "openinpresentation": 1,
        "boxes": [
            {
                "box": {
                    "fontname": "Ableton Sans Small",
                    "fontsize": 10.0,
                    "id": "obj-9",
                    "linecount": 3,
                    "maxclass": "live.comment",
                    "numinlets": 1,
                    "numoutlets": 0,
                    "patching_rect": [ 429.0, 333.0, 72.0, 42.0 ],
                    "presentation": 1,
                    "presentation_rect": [ 13.0, 276.0, 147.0, 18.0 ],
                    "text": "4. See the loading time here:",
                    "textjustification": 0
                }
            },
            {
                "box": {
                    "active": 0,
                    "fontname": "Ableton Sans Small",
                    "fontsize": 10.0,
                    "frozen_box_attributes": [ "active" ],
                    "id": "obj-7",
                    "maxclass": "live.numbox",
                    "numinlets": 1,
                    "numoutlets": 2,
                    "outlettype": [ "", "float" ],
                    "parameter_enable": 1,
                    "patching_rect": [ 510.0, 346.0, 50.0, 15.0 ],
                    "presentation": 1,
                    "presentation_rect": [ 13.0, 296.0, 163.0, 15.0 ],
                    "saved_attribute_attributes": {
                        "valueof": {
                            "parameter_longname": "live.numbox",
                            "parameter_mmax": 10000000.0,
                            "parameter_modmode": 3,
                            "parameter_shortname": "live.numbox",
                            "parameter_type": 0,
                            "parameter_unitstyle": 2
                        }
                    },
                    "varname": "live.numbox"
                }
            },
            {
                "box": {
                    "fontname": "Ableton Sans Small",
                    "fontsize": 10.0,
                    "id": "obj-5",
                    "maxclass": "live.comment",
                    "numinlets": 1,
                    "numoutlets": 0,
                    "patching_rect": [ 18.0, 20.0, 72.0, 18.0 ],
                    "presentation": 1,
                    "presentation_rect": [ 13.0, 209.0, 72.0, 18.0 ],
                    "text": "3. Press Load",
                    "textjustification": 0
                }
            },
            {
                "box": {
                    "fontname": "Ableton Sans Small",
                    "fontsize": 10.0,
                    "id": "obj-2",
                    "maxclass": "live.comment",
                    "numinlets": 1,
                    "numoutlets": 0,
                    "patching_rect": [ 95.0, 20.0, 142.0, 18.0 ],
                    "presentation": 1,
                    "presentation_rect": [ 13.0, 15.0, 142.0, 18.0 ],
                    "text": "1. Drop the Live Application",
                    "textjustification": 0
                }
            },
            {
                "box": {
                    "fontname": "Ableton Sans Small",
                    "fontsize": 10.0,
                    "id": "obj-1",
                    "maxclass": "live.comment",
                    "numinlets": 1,
                    "numoutlets": 0,
                    "patching_rect": [ 395.0, 20.0, 283.0, 18.0 ],
                    "presentation": 1,
                    "presentation_rect": [ 13.0, 112.0, 283.0, 18.0 ],
                    "text": "2. Drop the Live set file that contains DoneLoading.amxd",
                    "textjustification": 0
                }
            },
            {
                "box": {
                    "decodemode": 1,
                    "fontname": "Ableton Sans Small",
                    "fontsize": 10.0,
                    "id": "obj-6",
                    "maxclass": "live.drop",
                    "numinlets": 1,
                    "numoutlets": 2,
                    "outlettype": [ "", "" ],
                    "parameter_enable": 1,
                    "patching_rect": [ 95.0, 41.0, 284.0, 60.0 ],
                    "presentation": 1,
                    "presentation_rect": [ 13.0, 35.0, 284.0, 60.0 ],
                    "saved_attribute_attributes": {
                        "valueof": {
                            "parameter_invisible": 1,
                            "parameter_longname": "live.drop",
                            "parameter_modmode": 0,
                            "parameter_shortname": "live.drop",
                            "parameter_type": 4
                        }
                    },
                    "varname": "live.drop"
                }
            },
            {
                "box": {
                    "id": "obj-33",
                    "maxclass": "newobj",
                    "numinlets": 2,
                    "numoutlets": 1,
                    "outlettype": [ "float" ],
                    "patching_rect": [ 571.0, 346.0, 45.0, 22.0 ],
                    "text": "/ 1000."
                }
            },
            {
                "box": {
                    "fontname": "Arial",
                    "fontsize": 13.0,
                    "id": "obj-32",
                    "maxclass": "newobj",
                    "numinlets": 1,
                    "numoutlets": 2,
                    "outlettype": [ "", "int" ],
                    "patching_rect": [ 95.0, 113.0, 140.0, 23.0 ],
                    "text": "conformpath max boot"
                }
            },
            {
                "box": {
                    "fontname": "Arial",
                    "fontsize": 13.0,
                    "id": "obj-36",
                    "maxclass": "newobj",
                    "numinlets": 1,
                    "numoutlets": 2,
                    "outlettype": [ "", "int" ],
                    "patching_rect": [ 395.0, 113.0, 140.0, 23.0 ],
                    "text": "conformpath max boot"
                }
            },
            {
                "box": {
                    "fontname": "Ableton Sans Small",
                    "fontsize": 10.0,
                    "id": "obj-26",
                    "maxclass": "live.text",
                    "mode": 0,
                    "numinlets": 1,
                    "numoutlets": 2,
                    "outlettype": [ "", "" ],
                    "parameter_enable": 1,
                    "patching_rect": [ 35.0, 41.0, 44.0, 15.0 ],
                    "presentation": 1,
                    "presentation_rect": [ 13.0, 229.0, 44.0, 15.0 ],
                    "saved_attribute_attributes": {
                        "valueof": {
                            "parameter_enum": [ "val1", "val2" ],
                            "parameter_longname": "live.text",
                            "parameter_mmax": 1,
                            "parameter_modmode": 0,
                            "parameter_shortname": "live.text",
                            "parameter_type": 2
                        }
                    },
                    "text": "LOAD",
                    "varname": "live.text"
                }
            },
            {
                "box": {
                    "id": "obj-25",
                    "maxclass": "newobj",
                    "numinlets": 2,
                    "numoutlets": 1,
                    "outlettype": [ "float" ],
                    "patching_rect": [ 571.0, 306.0, 83.0, 22.0 ],
                    "text": "- 0."
                }
            },
            {
                "box": {
                    "id": "obj-24",
                    "maxclass": "newobj",
                    "numinlets": 2,
                    "numoutlets": 2,
                    "outlettype": [ "bang", "" ],
                    "patching_rect": [ 571.0, 228.0, 54.0, 22.0 ],
                    "text": "sel done"
                }
            },
            {
                "box": {
                    "id": "obj-23",
                    "maxclass": "newobj",
                    "numinlets": 1,
                    "numoutlets": 1,
                    "outlettype": [ "float" ],
                    "patching_rect": [ 571.0, 267.0, 55.0, 22.0 ],
                    "text": "cpuclock"
                }
            },
            {
                "box": {
                    "id": "obj-22",
                    "maxclass": "newobj",
                    "numinlets": 1,
                    "numoutlets": 1,
                    "outlettype": [ "float" ],
                    "patching_rect": [ 635.0, 267.0, 55.0, 22.0 ],
                    "text": "cpuclock"
                }
            },
            {
                "box": {
                    "id": "obj-21",
                    "maxclass": "newobj",
                    "numinlets": 2,
                    "numoutlets": 1,
                    "outlettype": [ "" ],
                    "patching_rect": [ 35.0, 230.0, 29.5, 22.0 ],
                    "text": "join"
                }
            },
            {
                "box": {
                    "id": "obj-20",
                    "maxclass": "newobj",
                    "numinlets": 2,
                    "numoutlets": 2,
                    "outlettype": [ "", "" ],
                    "patching_rect": [ 335.0, 191.0, 79.0, 22.0 ],
                    "text": "zl reg"
                }
            },
            {
                "box": {
                    "id": "obj-19",
                    "maxclass": "newobj",
                    "numinlets": 1,
                    "numoutlets": 3,
                    "outlettype": [ "bang", "bang", "bang" ],
                    "patching_rect": [ 35.0, 152.0, 619.0, 22.0 ],
                    "text": "t b b b"
                }
            },
            {
                "box": {
                    "id": "obj-18",
                    "maxclass": "newobj",
                    "numinlets": 2,
                    "numoutlets": 2,
                    "outlettype": [ "", "" ],
                    "patching_rect": [ 35.0, 191.0, 79.0, 22.0 ],
                    "text": "zl reg"
                }
            },
            {
                "box": {
                    "decodemode": 1,
                    "fontname": "Ableton Sans Small",
                    "fontsize": 10.0,
                    "id": "obj-13",
                    "maxclass": "live.drop",
                    "numinlets": 1,
                    "numoutlets": 2,
                    "outlettype": [ "", "" ],
                    "parameter_enable": 1,
                    "patching_rect": [ 395.0, 41.0, 284.0, 60.0 ],
                    "presentation": 1,
                    "presentation_rect": [ 13.0, 132.0, 284.0, 60.0 ],
                    "saved_attribute_attributes": {
                        "valueof": {
                            "parameter_invisible": 1,
                            "parameter_longname": "live.drop[2]",
                            "parameter_modmode": 0,
                            "parameter_shortname": "live.drop",
                            "parameter_type": 4
                        }
                    },
                    "varname": "live.drop[2]"
                }
            },
            {
                "box": {
                    "id": "obj-12",
                    "maxclass": "newobj",
                    "numinlets": 1,
                    "numoutlets": 0,
                    "patching_rect": [ 571.0, 385.0, 80.0, 22.0 ],
                    "text": "print seconds"
                }
            },
            {
                "box": {
                    "id": "obj-11",
                    "maxclass": "newobj",
                    "numinlets": 1,
                    "numoutlets": 1,
                    "outlettype": [ "" ],
                    "patching_rect": [ 571.0, 190.0, 97.0, 22.0 ],
                    "saved_object_attributes": {
                        "port": 1337
                    },
                    "text": "udpreceive 1337"
                }
            },
            {
                "box": {
                    "id": "obj-8",
                    "maxclass": "newobj",
                    "numinlets": 1,
                    "numoutlets": 1,
                    "outlettype": [ "" ],
                    "patching_rect": [ 35.0, 269.0, 97.0, 22.0 ],
                    "text": "prepend open -a"
                }
            },
            {
                "box": {
                    "id": "obj-4",
                    "maxclass": "newobj",
                    "numinlets": 1,
                    "numoutlets": 2,
                    "outlettype": [ "", "bang" ],
                    "patching_rect": [ 35.0, 308.0, 33.0, 22.0 ],
                    "saved_object_attributes": {
                        "shell": "(default)"
                    },
                    "text": "shell"
                }
            }
        ],
        "lines": [
            {
                "patchline": {
                    "destination": [ "obj-24", 0 ],
                    "source": [ "obj-11", 0 ]
                }
            },
            {
                "patchline": {
                    "destination": [ "obj-36", 0 ],
                    "source": [ "obj-13", 0 ]
                }
            },
            {
                "patchline": {
                    "destination": [ "obj-21", 0 ],
                    "source": [ "obj-18", 0 ]
                }
            },
            {
                "patchline": {
                    "destination": [ "obj-18", 0 ],
                    "source": [ "obj-19", 0 ]
                }
            },
            {
                "patchline": {
                    "destination": [ "obj-20", 0 ],
                    "source": [ "obj-19", 1 ]
                }
            },
            {
                "patchline": {
                    "destination": [ "obj-22", 0 ],
                    "source": [ "obj-19", 2 ]
                }
            },
            {
                "patchline": {
                    "destination": [ "obj-21", 1 ],
                    "source": [ "obj-20", 0 ]
                }
            },
            {
                "patchline": {
                    "destination": [ "obj-8", 0 ],
                    "source": [ "obj-21", 0 ]
                }
            },
            {
                "patchline": {
                    "destination": [ "obj-25", 1 ],
                    "source": [ "obj-22", 0 ]
                }
            },
            {
                "patchline": {
                    "destination": [ "obj-25", 0 ],
                    "source": [ "obj-23", 0 ]
                }
            },
            {
                "patchline": {
                    "destination": [ "obj-23", 0 ],
                    "source": [ "obj-24", 0 ]
                }
            },
            {
                "patchline": {
                    "destination": [ "obj-33", 0 ],
                    "order": 0,
                    "source": [ "obj-25", 0 ]
                }
            },
            {
                "patchline": {
                    "destination": [ "obj-7", 0 ],
                    "order": 1,
                    "source": [ "obj-25", 0 ]
                }
            },
            {
                "patchline": {
                    "destination": [ "obj-19", 0 ],
                    "source": [ "obj-26", 0 ]
                }
            },
            {
                "patchline": {
                    "destination": [ "obj-18", 1 ],
                    "source": [ "obj-32", 0 ]
                }
            },
            {
                "patchline": {
                    "destination": [ "obj-12", 0 ],
                    "source": [ "obj-33", 0 ]
                }
            },
            {
                "patchline": {
                    "destination": [ "obj-20", 1 ],
                    "source": [ "obj-36", 0 ]
                }
            },
            {
                "patchline": {
                    "destination": [ "obj-32", 0 ],
                    "source": [ "obj-6", 0 ]
                }
            },
            {
                "patchline": {
                    "destination": [ "obj-4", 0 ],
                    "source": [ "obj-8", 0 ]
                }
            }
        ],
        "parameters": {
            "obj-13": [ "live.drop[2]", "live.drop", 0 ],
            "obj-26": [ "live.text", "live.text", 0 ],
            "obj-6": [ "live.drop", "live.drop", 0 ],
            "obj-7": [ "live.numbox", "live.numbox", 0 ],
            "parameterbanks": {
                "0": {
                    "index": 0,
                    "name": "",
                    "parameters": [ "-", "-", "-", "-", "-", "-", "-", "-" ],
                    "buttons": [ "-", "-", "-", "-", "-", "-", "-", "-" ]
                }
            },
            "inherited_shortname": 1
        },
        "autosave": 0
    }
}