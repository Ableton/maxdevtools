# fmt: off
"""Exposes a dictionary representation of known objects that exist in Max."""

known_objects = {
    "boxes": [
        {
            "box": {
                "maxclass": "live.scope~",
                "numoutlets": 1,
                "outlettype": ["bang"],
                "patching_rect": [60.0, 60.0, 184.0, 68.0],
                "id": "obj-2",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "live.adsrui",
                "numoutlets": 10,
                "outlettype": ["", "", "", "", "", "", "", "", "", ""],
                "patching_rect": [140.0, 60.0, 184.0, 68.0],
                "id": "obj-4",
                "numinlets": 10,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "live.adsr~",
                "numoutlets": 3,
                "outlettype": ["signal", "signal", ""],
                "patching_rect": [220.0, 60.0, 124.0, 22.0],
                "id": "obj-5",
                "numinlets": 11,
            }
        },
        {
            "box": {
                "maxclass": "message",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [300.0, 60.0, 50.0, 22.0],
                "id": "obj-7",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "bgcolor",
                "numoutlets": 0,
                "patching_rect": [380.0, 60.0, 50.5, 22.0],
                "id": "obj-8",
                "numinlets": 4,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "patcher",
                "numoutlets": 0,
                "patching_rect": [460.0, 60.0, 49.0, 22.0],
                "id": "obj-9",
                "numinlets": 0,
                "patcher": {
                    "fileversion": 1,
                    "appversion": {
                        "major": 8,
                        "minor": 6,
                        "revision": 0,
                        "architecture": "x64",
                        "modernui": 1,
                    },
                    "classnamespace": "box",
                    "rect": [59.0, 106.0, 640.0, 480.0],
                    "bglocked": 0,
                    "openinpresentation": 0,
                    "default_fontsize": 12.0,
                    "default_fontface": 0,
                    "default_fontname": "Arial",
                    "gridonopen": 1,
                    "gridsize": [15.0, 15.0],
                    "gridsnaponopen": 1,
                    "objectsnaponopen": 1,
                    "statusbarvisible": 2,
                    "toolbarvisible": 1,
                    "lefttoolbarpinned": 0,
                    "toptoolbarpinned": 0,
                    "righttoolbarpinned": 0,
                    "bottomtoolbarpinned": 0,
                    "toolbars_unpinned_last_save": 0,
                    "tallnewobj": 0,
                    "boxanimatetime": 200,
                    "enablehscroll": 1,
                    "enablevscroll": 1,
                    "devicewidth": 0.0,
                    "description": "",
                    "digest": "",
                    "tags": "",
                    "style": "",
                    "subpatcher_template": "",
                    "assistshowspatchername": 0,
                    "boxes": [],
                    "lines": [],
                },
                "saved_object_attributes": {
                    "description": "",
                    "digest": "",
                    "globalpatchername": "",
                    "tags": "",
                },
            }
        },
        {
            "box": {
                "maxclass": "outlet",
                "numoutlets": 0,
                "patching_rect": [540.0, 60.0, 30.0, 30.0],
                "id": "obj-11",
                "numinlets": 1,
                "comment": "",
                "index": 1,
            }
        },
        {
            "box": {
                "maxclass": "inlet",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [620.0, 60.0, 30.0, 30.0],
                "id": "obj-13",
                "numinlets": 0,
                "comment": "",
                "index": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "send",
                "numoutlets": 0,
                "patching_rect": [700.0, 60.0, 35.0, 22.0],
                "id": "obj-14",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "append",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [780.0, 60.0, 49.0, 22.0],
                "id": "obj-15",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "prepend",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [860.0, 60.0, 53.0, 22.0],
                "id": "obj-16",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "int",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [940.0, 60.0, 29.5, 22.0],
                "id": "obj-17",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "float",
                "numoutlets": 1,
                "outlettype": ["float"],
                "patching_rect": [1020.0, 60.0, 31.0, 22.0],
                "id": "obj-18",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.3m",
                "numoutlets": 4,
                "outlettype": ["", "", "", ""],
                "patching_rect": [60.0, 85.0, 50.5, 22.0],
                "id": "obj-20",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.alphablend",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [140.0, 85.0, 79.0, 22.0],
                "id": "obj-21",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.altern",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [220.0, 85.0, 51.0, 22.0],
                "id": "obj-22",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.ameba",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [300.0, 85.0, 57.0, 22.0],
                "id": "obj-23",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.anim.drive",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [380.0, 85.0, 76.0, 22.0],
                "id": "obj-24",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.anim.node",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [460.0, 85.0, 77.0, 22.0],
                "id": "obj-25",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.anim.path",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [540.0, 85.0, 73.0, 22.0],
                "id": "obj-26",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.argb2ayuv",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [620.0, 85.0, 77.0, 22.0],
                "id": "obj-27",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.argb2grgb",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [700.0, 85.0, 75.0, 22.0],
                "id": "obj-28",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.argb2uyvy",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [780.0, 85.0, 76.0, 22.0],
                "id": "obj-30",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.avc",
                "numoutlets": 0,
                "patching_rect": [860.0, 85.0, 39.0, 22.0],
                "id": "obj-31",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.avg4",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [940.0, 85.0, 47.0, 22.0],
                "id": "obj-32",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.axis2quat",
                "numoutlets": 2,
                "outlettype": ["list", ""],
                "patching_rect": [1020.0, 85.0, 72.0, 22.0],
                "id": "obj-33",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.ayuv2argb",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [1100.0, 85.0, 77.0, 22.0],
                "id": "obj-34",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.ayuv2luma",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [1180.0, 85.0, 79.0, 22.0],
                "id": "obj-35",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.ayuv2uyvy",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [1260.0, 85.0, 77.0, 22.0],
                "id": "obj-36",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.bfg",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [1340.0, 85.0, 37.0, 22.0],
                "id": "obj-37",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.brass",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [1420.0, 85.0, 50.0, 22.0],
                "id": "obj-38",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.brcosa",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [1500.0, 85.0, 57.0, 22.0],
                "id": "obj-39",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.bsort",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [1580.0, 85.0, 47.0, 22.0],
                "id": "obj-40",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.buffer~",
                "numoutlets": 3,
                "outlettype": ["jit_matrix", "jit_matrix", ""],
                "patching_rect": [60.0, 110.0, 58.0, 22.0],
                "id": "obj-41",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.catch~",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [140.0, 110.0, 56.0, 22.0],
                "id": "obj-42",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.change",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [220.0, 110.0, 60.0, 22.0],
                "id": "obj-43",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.charmap",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [300.0, 110.0, 67.0, 22.0],
                "id": "obj-44",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.chromakey",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [380.0, 110.0, 79.0, 22.0],
                "id": "obj-45",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.clip",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [460.0, 110.0, 39.0, 22.0],
                "id": "obj-46",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.coerce",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [540.0, 110.0, 57.0, 22.0],
                "id": "obj-47",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.colorspace",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [620.0, 110.0, 79.0, 22.0],
                "id": "obj-48",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.concat",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [700.0, 110.0, 56.0, 22.0],
                "id": "obj-49",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.convolve",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [780.0, 110.0, 68.0, 22.0],
                "id": "obj-50",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.conway",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [860.0, 110.0, 61.0, 22.0],
                "id": "obj-51",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.cycle",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [940.0, 110.0, 48.0, 22.0],
                "id": "obj-52",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.demultiplex",
                "numoutlets": 3,
                "outlettype": ["jit_matrix", "jit_matrix", ""],
                "patching_rect": [1020.0, 110.0, 81.0, 22.0],
                "id": "obj-53",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.desktop",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [1100.0, 110.0, 63.0, 22.0],
                "id": "obj-54",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.dimmap",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [1180.0, 110.0, 63.0, 22.0],
                "id": "obj-55",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.dimop",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [1260.0, 110.0, 53.0, 22.0],
                "id": "obj-56",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.displays",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [1340.0, 110.0, 64.0, 22.0],
                "id": "obj-57",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.dx.grab",
                "numoutlets": 0,
                "patching_rect": [1420.0, 110.0, 61.0, 22.0],
                "id": "obj-58",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.dx.videoout",
                "numoutlets": 0,
                "patching_rect": [1500.0, 110.0, 82.0, 22.0],
                "id": "obj-59",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.eclipse",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [1580.0, 110.0, 58.0, 22.0],
                "id": "obj-60",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.euler2quat",
                "numoutlets": 2,
                "outlettype": ["list", ""],
                "patching_rect": [60.0, 135.0, 77.0, 22.0],
                "id": "obj-61",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.expr",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [140.0, 135.0, 44.0, 22.0],
                "id": "obj-62",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.fastblur",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [220.0, 135.0, 60.0, 22.0],
                "id": "obj-63",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.fft",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [300.0, 135.0, 30.0, 22.0],
                "id": "obj-64",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.fill",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [380.0, 135.0, 32.0, 22.0],
                "id": "obj-65",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.findbounds",
                "numoutlets": 3,
                "outlettype": ["", "", ""],
                "patching_rect": [460.0, 135.0, 79.0, 22.0],
                "id": "obj-66",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.fluoride",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [540.0, 135.0, 60.0, 22.0],
                "id": "obj-67",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.fprint",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [620.0, 135.0, 47.0, 22.0],
                "id": "obj-68",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "jit.fpsgui",
                "numoutlets": 2,
                "fontface": 0,
                "outlettype": ["", ""],
                "patching_rect": [700.0, 135.0, 80.0, 35.0],
                "id": "obj-70",
                "fontsize": 12.0,
                "numinlets": 1,
                "fontname": "Arial",
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.freeframe",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [780.0, 135.0, 72.0, 22.0],
                "id": "obj-71",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.gen",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [860.0, 135.0, 41.0, 22.0],
                "id": "obj-72",
                "numinlets": 2,
                "patcher": {
                    "fileversion": 1,
                    "appversion": {
                        "major": 8,
                        "minor": 6,
                        "revision": 0,
                        "architecture": "x64",
                        "modernui": 1,
                    },
                    "classnamespace": "jit.gen",
                    "rect": [0.0, 0.0, 600.0, 450.0],
                    "bglocked": 0,
                    "openinpresentation": 0,
                    "default_fontsize": 12.0,
                    "default_fontface": 0,
                    "default_fontname": "Arial",
                    "gridonopen": 1,
                    "gridsize": [15.0, 15.0],
                    "gridsnaponopen": 1,
                    "objectsnaponopen": 1,
                    "statusbarvisible": 2,
                    "toolbarvisible": 1,
                    "lefttoolbarpinned": 0,
                    "toptoolbarpinned": 0,
                    "righttoolbarpinned": 0,
                    "bottomtoolbarpinned": 0,
                    "toolbars_unpinned_last_save": 0,
                    "tallnewobj": 0,
                    "boxanimatetime": 200,
                    "enablehscroll": 1,
                    "enablevscroll": 1,
                    "devicewidth": 0.0,
                    "description": "",
                    "digest": "",
                    "tags": "",
                    "style": "",
                    "subpatcher_template": "",
                    "assistshowspatchername": 0,
                    "boxes": [
                        {
                            "box": {
                                "maxclass": "newobj",
                                "text": "in 1",
                                "numoutlets": 1,
                                "outlettype": [""],
                                "patching_rect": [50.0, 14.0, 28.0, 22.0],
                                "id": "obj-1",
                                "numinlets": 0,
                            }
                        },
                        {
                            "box": {
                                "maxclass": "newobj",
                                "text": "in 2",
                                "numoutlets": 1,
                                "outlettype": [""],
                                "patching_rect": [305.0, 14.0, 28.0, 22.0],
                                "id": "obj-2",
                                "numinlets": 0,
                            }
                        },
                        {
                            "box": {
                                "maxclass": "newobj",
                                "text": "+",
                                "numoutlets": 1,
                                "outlettype": [""],
                                "patching_rect": [176.0, 149.0, 29.5, 22.0],
                                "id": "obj-3",
                                "numinlets": 2,
                            }
                        },
                        {
                            "box": {
                                "maxclass": "newobj",
                                "text": "out 1",
                                "numoutlets": 0,
                                "patching_rect": [176.0, 418.0, 35.0, 22.0],
                                "id": "obj-4",
                                "numinlets": 1,
                            }
                        },
                    ],
                    "lines": [
                        {
                            "patchline": {
                                "source": ["obj-3", 0],
                                "destination": ["obj-4", 0],
                            }
                        },
                        {
                            "patchline": {
                                "source": ["obj-2", 0],
                                "destination": ["obj-3", 1],
                            }
                        },
                        {
                            "patchline": {
                                "source": ["obj-1", 0],
                                "destination": ["obj-3", 0],
                            }
                        },
                    ],
                },
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.gencoord",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [940.0, 135.0, 71.0, 22.0],
                "id": "obj-73",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.gl.asyncread",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [1020.0, 135.0, 89.0, 22.0],
                "id": "obj-74",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.gl.bfg",
                "numoutlets": 2,
                "outlettype": ["jit_gl_texture", ""],
                "patching_rect": [1100.0, 135.0, 50.0, 22.0],
                "id": "obj-75",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.gl.camera",
                "numoutlets": 2,
                "outlettype": ["jit_gl_texture", ""],
                "patching_rect": [1180.0, 135.0, 73.0, 22.0],
                "id": "obj-76",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.gl.cornerpin",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [1260.0, 135.0, 83.0, 22.0],
                "id": "obj-77",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.gl.cubemap",
                "numoutlets": 2,
                "outlettype": ["jit_gl_texture", ""],
                "patching_rect": [1340.0, 135.0, 83.0, 22.0],
                "id": "obj-78",
                "numinlets": 6,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.gl.graph",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [1420.0, 135.0, 64.0, 22.0],
                "id": "obj-79",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.gl.gridshape",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [1500.0, 135.0, 86.0, 22.0],
                "id": "obj-80",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.gl.handle",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [1580.0, 135.0, 69.0, 22.0],
                "id": "obj-81",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.gl.isosurf",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [60.0, 160.0, 69.0, 22.0],
                "id": "obj-82",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.gl.light",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [140.0, 160.0, 55.0, 22.0],
                "id": "obj-83",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.gl.lua",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [220.0, 160.0, 49.0, 22.0],
                "id": "obj-84",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.gl.material",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [300.0, 160.0, 92.5, 22.0],
                "id": "obj-85",
                "numinlets": 8,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.gl.mesh",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [380.0, 160.0, 103.0, 22.0],
                "id": "obj-86",
                "numinlets": 9,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.gl.model",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [460.0, 160.0, 66.0, 22.0],
                "id": "obj-87",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.gl.multiple",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [540.0, 160.0, 75.0, 22.0],
                "id": "obj-88",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.gl.node",
                "numoutlets": 3,
                "outlettype": ["jit_gl_texture", "", ""],
                "patching_rect": [620.0, 160.0, 60.0, 22.0],
                "id": "obj-89",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.gl.nurbs",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [700.0, 160.0, 63.0, 22.0],
                "id": "obj-90",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.gl.pass",
                "numoutlets": 3,
                "outlettype": ["jit_gl_texture", "", ""],
                "patching_rect": [780.0, 160.0, 59.0, 22.0],
                "id": "obj-91",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.gl.path",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [860.0, 160.0, 57.0, 22.0],
                "id": "obj-92",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.gl.physdraw",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [940.0, 160.0, 85.0, 22.0],
                "id": "obj-93",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.gl.picker",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [1020.0, 160.0, 65.0, 22.0],
                "id": "obj-94",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.gl.pix",
                "numoutlets": 2,
                "outlettype": ["jit_gl_texture", ""],
                "patching_rect": [1100.0, 160.0, 49.0, 22.0],
                "id": "obj-95",
                "numinlets": 2,
                "patcher": {
                    "fileversion": 1,
                    "appversion": {
                        "major": 8,
                        "minor": 6,
                        "revision": 0,
                        "architecture": "x64",
                        "modernui": 1,
                    },
                    "classnamespace": "jit.gen",
                    "rect": [0.0, 0.0, 600.0, 450.0],
                    "bglocked": 0,
                    "openinpresentation": 0,
                    "default_fontsize": 12.0,
                    "default_fontface": 0,
                    "default_fontname": "Arial",
                    "gridonopen": 1,
                    "gridsize": [15.0, 15.0],
                    "gridsnaponopen": 1,
                    "objectsnaponopen": 1,
                    "statusbarvisible": 2,
                    "toolbarvisible": 1,
                    "lefttoolbarpinned": 0,
                    "toptoolbarpinned": 0,
                    "righttoolbarpinned": 0,
                    "bottomtoolbarpinned": 0,
                    "toolbars_unpinned_last_save": 0,
                    "tallnewobj": 0,
                    "boxanimatetime": 200,
                    "enablehscroll": 1,
                    "enablevscroll": 1,
                    "devicewidth": 0.0,
                    "description": "",
                    "digest": "",
                    "tags": "",
                    "style": "",
                    "subpatcher_template": "",
                    "assistshowspatchername": 0,
                    "boxes": [
                        {
                            "box": {
                                "maxclass": "newobj",
                                "text": "in 1",
                                "numoutlets": 1,
                                "outlettype": [""],
                                "patching_rect": [50.0, 14.0, 28.0, 22.0],
                                "id": "obj-1",
                                "numinlets": 0,
                            }
                        },
                        {
                            "box": {
                                "maxclass": "newobj",
                                "text": "in 2",
                                "numoutlets": 1,
                                "outlettype": [""],
                                "patching_rect": [305.0, 14.0, 28.0, 22.0],
                                "id": "obj-2",
                                "numinlets": 0,
                            }
                        },
                        {
                            "box": {
                                "maxclass": "newobj",
                                "text": "+",
                                "numoutlets": 1,
                                "outlettype": [""],
                                "patching_rect": [176.0, 149.0, 29.5, 22.0],
                                "id": "obj-3",
                                "numinlets": 2,
                            }
                        },
                        {
                            "box": {
                                "maxclass": "newobj",
                                "text": "out 1",
                                "numoutlets": 0,
                                "patching_rect": [176.0, 418.0, 35.0, 22.0],
                                "id": "obj-4",
                                "numinlets": 1,
                            }
                        },
                    ],
                    "lines": [
                        {
                            "patchline": {
                                "source": ["obj-3", 0],
                                "destination": ["obj-4", 0],
                            }
                        },
                        {
                            "patchline": {
                                "source": ["obj-2", 0],
                                "destination": ["obj-3", 1],
                            }
                        },
                        {
                            "patchline": {
                                "source": ["obj-1", 0],
                                "destination": ["obj-3", 0],
                            }
                        },
                    ],
                },
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.gl.plato",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [1180.0, 160.0, 59.0, 22.0],
                "id": "obj-96",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.gl.render",
                "numoutlets": 2,
                "outlettype": ["bang", ""],
                "patching_rect": [1260.0, 160.0, 68.0, 22.0],
                "id": "obj-97",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.gl.shader",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [1340.0, 160.0, 70.0, 22.0],
                "id": "obj-98",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.gl.sketch",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [1420.0, 160.0, 68.0, 22.0],
                "id": "obj-99",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.gl.skybox",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [1500.0, 160.0, 71.0, 22.0],
                "id": "obj-100",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.gl.slab",
                "numoutlets": 2,
                "outlettype": ["jit_gl_texture", ""],
                "patching_rect": [1580.0, 160.0, 55.0, 22.0],
                "id": "obj-101",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.gl.text",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [60.0, 185.0, 53.0, 22.0],
                "id": "obj-102",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.gl.text2d",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [140.0, 185.0, 66.0, 22.0],
                "id": "obj-103",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.gl.text3d",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [220.0, 185.0, 66.0, 22.0],
                "id": "obj-104",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.gl.texture",
                "numoutlets": 2,
                "outlettype": ["jit_gl_texture", ""],
                "patching_rect": [300.0, 185.0, 70.0, 22.0],
                "id": "obj-105",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.gl.videoplane",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [380.0, 185.0, 91.0, 22.0],
                "id": "obj-106",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.gl.volume",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [460.0, 185.0, 72.0, 22.0],
                "id": "obj-107",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.glop",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [540.0, 185.0, 43.0, 22.0],
                "id": "obj-108",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.glue",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [620.0, 185.0, 43.0, 22.0],
                "id": "obj-109",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.grab",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [700.0, 185.0, 45.0, 22.0],
                "id": "obj-110",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.gradient",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [780.0, 185.0, 64.0, 22.0],
                "id": "obj-111",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.graph",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [860.0, 185.0, 51.0, 22.0],
                "id": "obj-112",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.grgb2argb",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [940.0, 185.0, 75.0, 22.0],
                "id": "obj-113",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.group-gl",
                "numoutlets": 0,
                "patching_rect": [1020.0, 185.0, 65.0, 22.0],
                "id": "obj-114",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.group-mop",
                "numoutlets": 0,
                "patching_rect": [1100.0, 185.0, 79.0, 22.0],
                "id": "obj-115",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.hatch",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [1180.0, 185.0, 50.0, 22.0],
                "id": "obj-116",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.hello",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [1260.0, 185.0, 46.0, 22.0],
                "id": "obj-117",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.histogram",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [1340.0, 185.0, 73.0, 22.0],
                "id": "obj-118",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.hsl2rgb",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [1420.0, 185.0, 60.0, 22.0],
                "id": "obj-119",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.hue",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [1500.0, 185.0, 41.0, 22.0],
                "id": "obj-120",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.iter",
                "numoutlets": 3,
                "outlettype": ["", "", ""],
                "patching_rect": [1580.0, 185.0, 37.0, 22.0],
                "id": "obj-121",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.keyscreen",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [60.0, 210.0, 75.0, 22.0],
                "id": "obj-122",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.la.determinant",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [140.0, 210.0, 97.0, 22.0],
                "id": "obj-123",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.la.diagproduct",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [220.0, 210.0, 96.0, 22.0],
                "id": "obj-124",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.la.inverse",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [300.0, 210.0, 72.0, 22.0],
                "id": "obj-125",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.la.mult",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [380.0, 210.0, 56.0, 22.0],
                "id": "obj-126",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.la.trace",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [460.0, 210.0, 60.0, 22.0],
                "id": "obj-127",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.la.uppertri",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [540.0, 210.0, 74.0, 22.0],
                "id": "obj-128",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.lcd",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [620.0, 210.0, 36.0, 22.0],
                "id": "obj-129",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.linden",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [700.0, 210.0, 53.0, 22.0],
                "id": "obj-130",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.luma2ayuv",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [780.0, 210.0, 79.0, 22.0],
                "id": "obj-131",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.luma2uyvy",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [860.0, 210.0, 78.0, 22.0],
                "id": "obj-132",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.lumakey",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [940.0, 210.0, 65.0, 22.0],
                "id": "obj-133",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.map",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [1020.0, 210.0, 44.0, 22.0],
                "id": "obj-134",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.matrix",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [1100.0, 210.0, 53.0, 22.0],
                "id": "obj-135",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.matrixinfo",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [1180.0, 210.0, 73.0, 22.0],
                "id": "obj-136",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.matrixset",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [1260.0, 210.0, 69.0, 22.0],
                "id": "obj-137",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.mgraphics",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [1340.0, 210.0, 76.0, 22.0],
                "id": "obj-138",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.movie",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [1420.0, 210.0, 53.0, 22.0],
                "id": "obj-139",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.multiplex",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [1500.0, 210.0, 68.0, 22.0],
                "id": "obj-140",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.mxform2d",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [1580.0, 210.0, 74.0, 22.0],
                "id": "obj-141",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.net.recv",
                "numoutlets": 3,
                "outlettype": ["jit_matrix", "", ""],
                "patching_rect": [60.0, 235.0, 63.0, 22.0],
                "id": "obj-142",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.net.send",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [140.0, 235.0, 67.0, 22.0],
                "id": "obj-143",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.noise",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [220.0, 235.0, 49.0, 22.0],
                "id": "obj-144",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.normalize",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [300.0, 235.0, 73.0, 22.0],
                "id": "obj-145",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.obref",
                "numoutlets": 0,
                "patching_rect": [380.0, 235.0, 48.0, 22.0],
                "id": "obj-146",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.op",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [460.0, 235.0, 34.0, 22.0],
                "id": "obj-147",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.openexr",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [540.0, 235.0, 64.0, 22.0],
                "id": "obj-148",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.p.bounds",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [620.0, 235.0, 70.0, 22.0],
                "id": "obj-149",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.p.shiva",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [700.0, 235.0, 59.0, 22.0],
                "id": "obj-150",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.p.vishnu",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [780.0, 235.0, 65.0, 22.0],
                "id": "obj-151",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.pack",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [860.0, 235.0, 46.0, 22.0],
                "id": "obj-152",
                "numinlets": 4,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.path",
                "numoutlets": 4,
                "outlettype": ["jit_matrix", "jit_matrix", "", ""],
                "patching_rect": [940.0, 235.0, 44.0, 22.0],
                "id": "obj-153",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.peek~",
                "numoutlets": 2,
                "outlettype": ["signal", ""],
                "patching_rect": [1020.0, 235.0, 54.0, 22.0],
                "id": "obj-154",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.phys.6dof",
                "numoutlets": 3,
                "outlettype": ["", "", ""],
                "patching_rect": [1100.0, 235.0, 73.0, 22.0],
                "id": "obj-155",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.phys.barslide",
                "numoutlets": 3,
                "outlettype": ["", "", ""],
                "patching_rect": [1180.0, 235.0, 91.0, 22.0],
                "id": "obj-156",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.phys.body",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [1260.0, 235.0, 75.0, 22.0],
                "id": "obj-157",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.phys.conetwist",
                "numoutlets": 3,
                "outlettype": ["", "", ""],
                "patching_rect": [1340.0, 235.0, 99.0, 22.0],
                "id": "obj-158",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.phys.ghost",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [1420.0, 235.0, 79.0, 22.0],
                "id": "obj-159",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.phys.hinge",
                "numoutlets": 3,
                "outlettype": ["", "", ""],
                "patching_rect": [1500.0, 235.0, 79.0, 22.0],
                "id": "obj-160",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.phys.multiple",
                "numoutlets": 3,
                "outlettype": ["jit_matrix", "jit_matrix", ""],
                "patching_rect": [1580.0, 235.0, 91.0, 22.0],
                "id": "obj-161",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.phys.picker",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [60.0, 260.0, 81.0, 22.0],
                "id": "obj-162",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.phys.point2point",
                "numoutlets": 3,
                "outlettype": ["", "", ""],
                "patching_rect": [140.0, 260.0, 108.0, 22.0],
                "id": "obj-163",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.phys.world",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [220.0, 260.0, 78.0, 22.0],
                "id": "obj-164",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.pix",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [300.0, 260.0, 36.0, 22.0],
                "id": "obj-165",
                "numinlets": 2,
                "patcher": {
                    "fileversion": 1,
                    "appversion": {
                        "major": 8,
                        "minor": 6,
                        "revision": 0,
                        "architecture": "x64",
                        "modernui": 1,
                    },
                    "classnamespace": "jit.gen",
                    "rect": [0.0, 0.0, 600.0, 450.0],
                    "bglocked": 0,
                    "openinpresentation": 0,
                    "default_fontsize": 12.0,
                    "default_fontface": 0,
                    "default_fontname": "Arial",
                    "gridonopen": 1,
                    "gridsize": [15.0, 15.0],
                    "gridsnaponopen": 1,
                    "objectsnaponopen": 1,
                    "statusbarvisible": 2,
                    "toolbarvisible": 1,
                    "lefttoolbarpinned": 0,
                    "toptoolbarpinned": 0,
                    "righttoolbarpinned": 0,
                    "bottomtoolbarpinned": 0,
                    "toolbars_unpinned_last_save": 0,
                    "tallnewobj": 0,
                    "boxanimatetime": 200,
                    "enablehscroll": 1,
                    "enablevscroll": 1,
                    "devicewidth": 0.0,
                    "description": "",
                    "digest": "",
                    "tags": "",
                    "style": "",
                    "subpatcher_template": "",
                    "assistshowspatchername": 0,
                    "boxes": [
                        {
                            "box": {
                                "maxclass": "newobj",
                                "text": "in 1",
                                "numoutlets": 1,
                                "outlettype": [""],
                                "patching_rect": [50.0, 14.0, 28.0, 22.0],
                                "id": "obj-1",
                                "numinlets": 0,
                            }
                        },
                        {
                            "box": {
                                "maxclass": "newobj",
                                "text": "in 2",
                                "numoutlets": 1,
                                "outlettype": [""],
                                "patching_rect": [305.0, 14.0, 28.0, 22.0],
                                "id": "obj-2",
                                "numinlets": 0,
                            }
                        },
                        {
                            "box": {
                                "maxclass": "newobj",
                                "text": "+",
                                "numoutlets": 1,
                                "outlettype": [""],
                                "patching_rect": [176.0, 149.0, 29.5, 22.0],
                                "id": "obj-3",
                                "numinlets": 2,
                            }
                        },
                        {
                            "box": {
                                "maxclass": "newobj",
                                "text": "out 1",
                                "numoutlets": 0,
                                "patching_rect": [176.0, 418.0, 35.0, 22.0],
                                "id": "obj-4",
                                "numinlets": 1,
                            }
                        },
                    ],
                    "lines": [
                        {
                            "patchline": {
                                "source": ["obj-3", 0],
                                "destination": ["obj-4", 0],
                            }
                        },
                        {
                            "patchline": {
                                "source": ["obj-2", 0],
                                "destination": ["obj-3", 1],
                            }
                        },
                        {
                            "patchline": {
                                "source": ["obj-1", 0],
                                "destination": ["obj-3", 0],
                            }
                        },
                    ],
                },
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.planeop",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [380.0, 260.0, 63.0, 22.0],
                "id": "obj-166",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "jit.playlist",
                "output_texture": 0,
                "loop": 0,
                "numoutlets": 3,
                "outlettype": ["jit_matrix", "", "dictionary"],
                "patching_rect": [460.0, 260.0, 150.0, 92.0],
                "id": "obj-168",
                "drawto": "",
                "numinlets": 1,
                "parameter_enable": 0,
                "data": {"clips": []},
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.plot",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [540.0, 260.0, 40.0, 22.0],
                "id": "obj-169",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.plume",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [620.0, 260.0, 53.0, 22.0],
                "id": "obj-170",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.plur",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [700.0, 260.0, 41.0, 22.0],
                "id": "obj-171",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.poke~",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [780.0, 260.0, 54.0, 22.0],
                "id": "obj-172",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.print",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [860.0, 260.0, 44.0, 22.0],
                "id": "obj-173",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.proxy",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [940.0, 260.0, 50.0, 22.0],
                "id": "obj-174",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "jit.pwindow",
                "numoutlets": 2,
                "sync": 1,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [1020.0, 260.0, 80.0, 60.0],
                "id": "obj-176",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "jit.pworld",
                "enable": 1,
                "numoutlets": 2,
                "sync": 1,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [1100.0, 260.0, 80.0, 60.0],
                "id": "obj-178",
                "fps": 30.0,
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.qball",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [1180.0, 260.0, 46.0, 22.0],
                "id": "obj-179",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.qfaker",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [1260.0, 260.0, 54.0, 22.0],
                "id": "obj-180",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.qt.grab",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [1340.0, 260.0, 58.0, 22.0],
                "id": "obj-181",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.qt.movie",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [1420.0, 260.0, 66.0, 22.0],
                "id": "obj-182",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.qt.record",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [1500.0, 260.0, 68.0, 22.0],
                "id": "obj-183",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.qt.videoout",
                "numoutlets": 0,
                "patching_rect": [1580.0, 260.0, 79.0, 22.0],
                "id": "obj-184",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.quat",
                "numoutlets": 2,
                "outlettype": ["list", ""],
                "patching_rect": [60.0, 285.0, 44.0, 22.0],
                "id": "obj-185",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.quat2axis",
                "numoutlets": 2,
                "outlettype": ["list", ""],
                "patching_rect": [140.0, 285.0, 72.0, 22.0],
                "id": "obj-186",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.quat2euler",
                "numoutlets": 2,
                "outlettype": ["list", ""],
                "patching_rect": [220.0, 285.0, 77.0, 22.0],
                "id": "obj-187",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.record",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [300.0, 285.0, 55.0, 22.0],
                "id": "obj-188",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.release~",
                "numoutlets": 2,
                "outlettype": ["signal", ""],
                "patching_rect": [380.0, 285.0, 67.0, 22.0],
                "id": "obj-189",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.repos",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [460.0, 285.0, 51.0, 22.0],
                "id": "obj-190",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.resamp",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [540.0, 285.0, 61.0, 22.0],
                "id": "obj-191",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.reverse",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [620.0, 285.0, 61.0, 22.0],
                "id": "obj-192",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.rgb2hsl",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [700.0, 285.0, 60.0, 22.0],
                "id": "obj-193",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.rgb2luma",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [780.0, 285.0, 71.0, 22.0],
                "id": "obj-194",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.robcross",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [860.0, 285.0, 67.0, 22.0],
                "id": "obj-195",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.rota",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [940.0, 285.0, 41.0, 22.0],
                "id": "obj-196",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.roy",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [1020.0, 285.0, 37.0, 22.0],
                "id": "obj-197",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.rubix",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [1100.0, 285.0, 47.0, 22.0],
                "id": "obj-198",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.scalebias",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [1180.0, 285.0, 71.0, 22.0],
                "id": "obj-199",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.scanoffset",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [1260.0, 285.0, 75.0, 22.0],
                "id": "obj-200",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.scanslide",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [1340.0, 285.0, 71.0, 22.0],
                "id": "obj-201",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.scanwrap",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [1420.0, 285.0, 72.0, 22.0],
                "id": "obj-202",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.scissors",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [1500.0, 285.0, 64.0, 22.0],
                "id": "obj-203",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "jit.scope",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [1580.0, 285.0, 80.0, 60.0],
                "id": "obj-205",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.shade",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [60.0, 310.0, 53.0, 22.0],
                "id": "obj-206",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.slide",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [140.0, 310.0, 45.0, 22.0],
                "id": "obj-207",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.sobel",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [220.0, 310.0, 49.0, 22.0],
                "id": "obj-208",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.spill",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [300.0, 310.0, 41.0, 22.0],
                "id": "obj-209",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.split",
                "numoutlets": 3,
                "outlettype": ["jit_matrix", "jit_matrix", ""],
                "patching_rect": [380.0, 310.0, 42.0, 22.0],
                "id": "obj-210",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.sprinkle",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [460.0, 310.0, 62.0, 22.0],
                "id": "obj-211",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.str.fromsymbol",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [540.0, 310.0, 99.0, 22.0],
                "id": "obj-212",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.str.op",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [620.0, 310.0, 50.0, 22.0],
                "id": "obj-213",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.str.regexp",
                "numoutlets": 5,
                "outlettype": [
                    "jit_matrix",
                    "jit_matrix",
                    "jit_matrix",
                    "jit_matrix",
                    "",
                ],
                "patching_rect": [700.0, 310.0, 73.0, 22.0],
                "id": "obj-214",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.str.tosymbol",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [780.0, 310.0, 85.0, 22.0],
                "id": "obj-215",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.streak",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [860.0, 310.0, 53.0, 22.0],
                "id": "obj-216",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.submatrix",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [940.0, 310.0, 73.0, 22.0],
                "id": "obj-217",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.textfile",
                "numoutlets": 3,
                "outlettype": ["jit_matrix", "jit_matrix", ""],
                "patching_rect": [1020.0, 310.0, 55.0, 22.0],
                "id": "obj-218",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.thin",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [1100.0, 310.0, 40.0, 22.0],
                "id": "obj-219",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.tiffany",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [1180.0, 310.0, 52.0, 22.0],
                "id": "obj-220",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.traffic",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [1260.0, 310.0, 50.0, 22.0],
                "id": "obj-221",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.transpose",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [1340.0, 310.0, 73.0, 22.0],
                "id": "obj-222",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.turtle",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [1420.0, 310.0, 47.0, 22.0],
                "id": "obj-223",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.uldl",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [1500.0, 310.0, 39.0, 22.0],
                "id": "obj-224",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.unpack",
                "numoutlets": 5,
                "outlettype": [
                    "jit_matrix",
                    "jit_matrix",
                    "jit_matrix",
                    "jit_matrix",
                    "",
                ],
                "patching_rect": [1580.0, 310.0, 59.0, 22.0],
                "id": "obj-225",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.uyvy2argb",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [60.0, 335.0, 76.0, 22.0],
                "id": "obj-226",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.uyvy2ayuv",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [140.0, 335.0, 77.0, 22.0],
                "id": "obj-227",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.uyvy2luma",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [220.0, 335.0, 78.0, 22.0],
                "id": "obj-228",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.vcr",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [300.0, 335.0, 36.0, 22.0],
                "id": "obj-229",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.wake",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [380.0, 335.0, 49.0, 22.0],
                "id": "obj-230",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.window",
                "numoutlets": 2,
                "outlettype": ["bang", ""],
                "patching_rect": [460.0, 335.0, 61.0, 22.0],
                "id": "obj-231",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.world",
                "numoutlets": 3,
                "outlettype": ["jit_matrix", "bang", ""],
                "patching_rect": [540.0, 335.0, 49.0, 22.0],
                "id": "obj-232",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.xfade",
                "numoutlets": 2,
                "outlettype": ["jit_matrix", ""],
                "patching_rect": [620.0, 335.0, 50.0, 22.0],
                "id": "obj-233",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.jit.peek~",
                "numoutlets": 3,
                "outlettype": ["multichannelsignal", "", ""],
                "patching_rect": [700.0, 335.0, 73.0, 22.0],
                "id": "obj-234",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "chucker~",
                "numoutlets": 3,
                "outlettype": ["signal", "signal", "signal"],
                "patching_rect": [780.0, 335.0, 58.0, 22.0],
                "id": "obj-235",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "cverb~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [860.0, 335.0, 45.0, 22.0],
                "id": "obj-236",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "ddg.mono",
                "numoutlets": 2,
                "outlettype": ["int", "int"],
                "patching_rect": [940.0, 335.0, 62.0, 22.0],
                "id": "obj-237",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "live.arrows",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [1020.0, 335.0, 70.0, 15.0],
                "id": "obj-239",
                "numinlets": 1,
                "parameter_enable": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "live.banks",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [1100.0, 335.0, 62.0, 22.0],
                "id": "obj-240",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "live.button",
                "varname": "live.button",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [1180.0, 335.0, 15.0, 15.0],
                "id": "obj-242",
                "numinlets": 1,
                "parameter_enable": 1,
                "saved_attribute_attributes": {
                    "valueof": {
                        "parameter_enum": ["off", "on"],
                        "parameter_longname": "live.button",
                        "parameter_mmax": 1,
                        "parameter_shortname": "live.button",
                        "parameter_type": 2,
                    }
                },
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "live.colors",
                "numoutlets": 2,
                "outlettype": ["", "bang"],
                "patching_rect": [1260.0, 335.0, 62.0, 22.0],
                "id": "obj-243",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "live.comment",
                "numoutlets": 0,
                "patching_rect": [1340.0, 335.0, 150.0, 18.0],
                "id": "obj-245",
                "textjustification": 0,
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "live.dial",
                "varname": "live.dial",
                "numoutlets": 2,
                "outlettype": ["", "float"],
                "patching_rect": [1420.0, 335.0, 41.0, 48.0],
                "id": "obj-247",
                "numinlets": 1,
                "parameter_enable": 1,
                "saved_attribute_attributes": {
                    "valueof": {
                        "parameter_longname": "live.dial",
                        "parameter_shortname": "live.dial",
                        "parameter_type": 0,
                        "parameter_unitstyle": 0,
                    }
                },
            }
        },
        {
            "box": {
                "maxclass": "live.drop",
                "varname": "live.drop",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [1500.0, 335.0, 140.0, 60.0],
                "id": "obj-249",
                "decodemode": 1,
                "numinlets": 1,
                "parameter_enable": 1,
                "saved_attribute_attributes": {
                    "valueof": {
                        "parameter_invisible": 1,
                        "parameter_longname": "live.drop",
                        "parameter_shortname": "live.drop",
                        "parameter_type": 4,
                    }
                },
            }
        },
        {
            "box": {
                "maxclass": "live.gain~",
                "varname": "live.gain~",
                "numoutlets": 5,
                "outlettype": ["signal", "signal", "", "float", "list"],
                "lastchannelcount": 0,
                "patching_rect": [1580.0, 335.0, 48.0, 136.0],
                "id": "obj-251",
                "numinlets": 2,
                "parameter_enable": 1,
                "saved_attribute_attributes": {
                    "valueof": {
                        "parameter_longname": "live.gain~",
                        "parameter_mmax": 6.0,
                        "parameter_mmin": -70.0,
                        "parameter_shortname": "live.gain~",
                        "parameter_type": 0,
                        "parameter_unitstyle": 4,
                    }
                },
            }
        },
        {
            "box": {
                "maxclass": "live.grid",
                "varname": "live.grid",
                "numoutlets": 6,
                "outlettype": ["", "", "", "", "", ""],
                "patching_rect": [60.0, 360.0, 300.0, 150.0],
                "id": "obj-253",
                "numinlets": 2,
                "parameter_enable": 1,
                "saved_attribute_attributes": {
                    "valueof": {
                        "parameter_invisible": 1,
                        "parameter_longname": "live.grid",
                        "parameter_shortname": "live.grid",
                        "parameter_type": 3,
                    }
                },
            }
        },
        {
            "box": {
                "maxclass": "live.line",
                "numoutlets": 0,
                "patching_rect": [140.0, 360.0, 5.0, 100.0],
                "id": "obj-255",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "live.map",
                "numoutlets": 5,
                "outlettype": ["", "", "", "int", ""],
                "patching_rect": [220.0, 360.0, 53.0, 22.0],
                "id": "obj-256",
                "numinlets": 1,
                "saved_object_attributes": {"_persistence": 1},
            }
        },
        {
            "box": {
                "maxclass": "live.menu",
                "varname": "live.menu",
                "numoutlets": 3,
                "outlettype": ["", "", "float"],
                "patching_rect": [300.0, 360.0, 100.0, 15.0],
                "id": "obj-258",
                "numinlets": 1,
                "parameter_enable": 1,
                "saved_attribute_attributes": {
                    "valueof": {
                        "parameter_enum": ["one", "two", "three"],
                        "parameter_longname": "live.menu",
                        "parameter_mmax": 2,
                        "parameter_shortname": "live.menu",
                        "parameter_type": 2,
                    }
                },
            }
        },
        {
            "box": {
                "maxclass": "live.meter~",
                "numoutlets": 2,
                "slidercolor": [
                    0.141176470588235,
                    0.141176470588235,
                    0.141176470588235,
                    1.0,
                ],
                "outlettype": ["float", "int"],
                "patching_rect": [380.0, 360.0, 5.0, 100.0],
                "id": "obj-260",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "live.modulate~",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [460.0, 360.0, 86.0, 22.0],
                "id": "obj-261",
                "numinlets": 2,
                "saved_object_attributes": {
                    "_persistence": 1,
                    "depth": 1.0,
                    "smoothing": 1.0,
                },
            }
        },
        {
            "box": {
                "maxclass": "live.numbox",
                "varname": "live.numbox",
                "numoutlets": 2,
                "outlettype": ["", "float"],
                "patching_rect": [540.0, 360.0, 44.0, 15.0],
                "id": "obj-263",
                "numinlets": 1,
                "parameter_enable": 1,
                "saved_attribute_attributes": {
                    "valueof": {
                        "parameter_longname": "live.numbox",
                        "parameter_shortname": "live.numbox",
                        "parameter_type": 0,
                        "parameter_unitstyle": 0,
                    }
                },
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "live.object",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [620.0, 360.0, 62.0, 22.0],
                "id": "obj-264",
                "numinlets": 2,
                "saved_object_attributes": {"_persistence": 1},
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "live.observer",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [700.0, 360.0, 77.0, 22.0],
                "id": "obj-265",
                "numinlets": 2,
                "saved_object_attributes": {"_persistence": 1},
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "live.param~",
                "numoutlets": 0,
                "patching_rect": [780.0, 360.0, 71.0, 22.0],
                "id": "obj-266",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "live.path",
                "numoutlets": 3,
                "outlettype": ["", "", ""],
                "patching_rect": [860.0, 360.0, 53.0, 22.0],
                "id": "obj-267",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "live.remote~",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [940.0, 360.0, 74.0, 22.0],
                "id": "obj-268",
                "numinlets": 2,
                "saved_object_attributes": {
                    "_persistence": 1,
                    "normalized": 0,
                    "smoothing": 1.0,
                },
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "live.routing",
                "numoutlets": 5,
                "outlettype": ["", "", "", "", ""],
                "patching_rect": [1020.0, 360.0, 67.0, 22.0],
                "id": "obj-269",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "live.slider",
                "varname": "live.slider",
                "numoutlets": 2,
                "outlettype": ["", "float"],
                "patching_rect": [1100.0, 360.0, 39.0, 95.0],
                "id": "obj-271",
                "numinlets": 1,
                "parameter_enable": 1,
                "saved_attribute_attributes": {
                    "valueof": {
                        "parameter_longname": "live.slider",
                        "parameter_shortname": "live.slider",
                        "parameter_type": 0,
                        "parameter_unitstyle": 0,
                    }
                },
            }
        },
        {
            "box": {
                "maxclass": "live.step",
                "varname": "live.step",
                "numoutlets": 5,
                "outlettype": ["", "", "", "", ""],
                "patching_rect": [1180.0, 360.0, 400.0, 170.0],
                "id": "obj-273",
                "numinlets": 1,
                "parameter_enable": 1,
                "saved_attribute_attributes": {
                    "valueof": {
                        "parameter_invisible": 1,
                        "parameter_longname": "live.step",
                        "parameter_shortname": "live.step",
                        "parameter_type": 3,
                    }
                },
            }
        },
        {
            "box": {
                "maxclass": "live.tab",
                "varname": "live.tab",
                "num_lines_presentation": 0,
                "numoutlets": 3,
                "outlettype": ["", "", "float"],
                "patching_rect": [1260.0, 360.0, 100.0, 20.0],
                "id": "obj-275",
                "num_lines_patching": 1,
                "numinlets": 1,
                "parameter_enable": 1,
                "saved_attribute_attributes": {
                    "valueof": {
                        "parameter_enum": ["one", "two", "three"],
                        "parameter_longname": "live.tab",
                        "parameter_mmax": 2,
                        "parameter_shortname": "live.tab",
                        "parameter_type": 2,
                        "parameter_unitstyle": 9,
                    }
                },
            }
        },
        {
            "box": {
                "maxclass": "live.text",
                "varname": "live.text",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [1340.0, 360.0, 44.0, 15.0],
                "id": "obj-277",
                "numinlets": 1,
                "parameter_enable": 1,
                "saved_attribute_attributes": {
                    "valueof": {
                        "parameter_enum": ["val1", "val2"],
                        "parameter_longname": "live.text",
                        "parameter_mmax": 1,
                        "parameter_shortname": "live.text",
                        "parameter_type": 2,
                    }
                },
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "live.thisdevice",
                "numoutlets": 3,
                "outlettype": ["bang", "int", "int"],
                "patching_rect": [1420.0, 360.0, 83.0, 22.0],
                "id": "obj-278",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "live.toggle",
                "varname": "live.toggle",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [1500.0, 360.0, 15.0, 15.0],
                "id": "obj-280",
                "numinlets": 1,
                "parameter_enable": 1,
                "saved_attribute_attributes": {
                    "valueof": {
                        "parameter_enum": ["off", "on"],
                        "parameter_longname": "live.toggle",
                        "parameter_mmax": 1,
                        "parameter_shortname": "live.toggle",
                        "parameter_type": 2,
                    }
                },
            }
        },
        {
            "box": {
                "maxclass": "mc.live.gain~",
                "varname": "mc.live.gain~",
                "numoutlets": 4,
                "outlettype": ["multichannelsignal", "", "float", "list"],
                "lastchannelcount": 0,
                "patching_rect": [1580.0, 360.0, 48.0, 136.0],
                "id": "obj-282",
                "numinlets": 1,
                "parameter_enable": 1,
                "saved_attribute_attributes": {
                    "valueof": {
                        "parameter_longname": "mc.live.gain~",
                        "parameter_mmax": 6.0,
                        "parameter_mmin": -70.0,
                        "parameter_shortname": "mc.live.gain~",
                        "parameter_type": 0,
                        "parameter_unitstyle": 4,
                    }
                },
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "midiselect",
                "numoutlets": 8,
                "outlettype": ["", "", "", "int", "int", "", "int", "int"],
                "patching_rect": [60.0, 385.0, 62.0, 22.0],
                "id": "obj-283",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "parameters",
                "numoutlets": 0,
                "patching_rect": [140.0, 385.0, 69.0, 22.0],
                "id": "obj-284",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "paraminspector",
                "numoutlets": 0,
                "patching_rect": [220.0, 385.0, 91.0, 22.0],
                "id": "obj-285",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "abs",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [300.0, 385.0, 28.0, 22.0],
                "id": "obj-286",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "absolutepath",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [380.0, 385.0, 77.0, 22.0],
                "id": "obj-287",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "accum",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [460.0, 385.0, 44.0, 22.0],
                "id": "obj-288",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "acos",
                "numoutlets": 1,
                "outlettype": ["float"],
                "patching_rect": [540.0, 385.0, 34.0, 22.0],
                "id": "obj-289",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "acosh",
                "numoutlets": 1,
                "outlettype": ["float"],
                "patching_rect": [620.0, 385.0, 41.0, 22.0],
                "id": "obj-290",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "active",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [700.0, 385.0, 40.0, 22.0],
                "id": "obj-291",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "anal",
                "numoutlets": 1,
                "outlettype": ["list"],
                "patching_rect": [780.0, 385.0, 31.0, 22.0],
                "id": "obj-292",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "array.compare",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [860.0, 385.0, 85.0, 22.0],
                "id": "obj-293",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "array.concat",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [940.0, 385.0, 74.0, 22.0],
                "id": "obj-294",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "array.every",
                "numoutlets": 3,
                "outlettype": ["int", "", "int"],
                "patching_rect": [1020.0, 385.0, 68.0, 22.0],
                "id": "obj-295",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "array.filter",
                "numoutlets": 3,
                "outlettype": ["", "", "int"],
                "patching_rect": [1100.0, 385.0, 61.0, 22.0],
                "id": "obj-296",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "array.flatten",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [1180.0, 385.0, 71.0, 22.0],
                "id": "obj-297",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "array.foreach",
                "numoutlets": 3,
                "outlettype": ["bang", "", "int"],
                "patching_rect": [1260.0, 385.0, 78.0, 22.0],
                "id": "obj-298",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "array.frombuffer",
                "numoutlets": 2,
                "outlettype": ["", "int"],
                "patching_rect": [1340.0, 385.0, 93.0, 22.0],
                "id": "obj-299",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "array.index",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [1420.0, 385.0, 67.0, 22.0],
                "id": "obj-300",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "array.indexmap",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [1500.0, 385.0, 90.0, 22.0],
                "id": "obj-301",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "array.indexof",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [1580.0, 385.0, 77.0, 22.0],
                "id": "obj-302",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "array.iter",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [60.0, 410.0, 55.0, 22.0],
                "id": "obj-303",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "array.join",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [140.0, 410.0, 57.0, 22.0],
                "id": "obj-304",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "array.length",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [220.0, 410.0, 71.0, 22.0],
                "id": "obj-305",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "array.map",
                "numoutlets": 3,
                "outlettype": ["", "", "int"],
                "patching_rect": [300.0, 410.0, 62.0, 22.0],
                "id": "obj-306",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "array",
                "numoutlets": 3,
                "outlettype": ["", "", ""],
                "patching_rect": [380.0, 410.0, 36.0, 22.0],
                "id": "obj-307",
                "numinlets": 2,
                "saved_object_attributes": {
                    "parameter_enable": 0,
                    "parameter_mappable": 0,
                },
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "array.pop",
                "numoutlets": 3,
                "outlettype": ["bang", "", ""],
                "patching_rect": [460.0, 410.0, 58.0, 22.0],
                "id": "obj-308",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "array.push",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [540.0, 410.0, 64.0, 22.0],
                "id": "obj-309",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "array.remove",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [620.0, 410.0, 78.0, 22.0],
                "id": "obj-310",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "array.reverse",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [700.0, 410.0, 78.0, 22.0],
                "id": "obj-311",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "array.rotate",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [780.0, 410.0, 69.0, 22.0],
                "id": "obj-312",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "array.scramble",
                "numoutlets": 2,
                "outlettype": ["", "list"],
                "patching_rect": [860.0, 410.0, 87.0, 22.0],
                "id": "obj-313",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "array.sect",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [940.0, 410.0, 60.0, 22.0],
                "id": "obj-314",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "array.shift",
                "numoutlets": 3,
                "outlettype": ["bang", "", ""],
                "patching_rect": [1020.0, 410.0, 60.0, 22.0],
                "id": "obj-315",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "array.slice",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [1100.0, 410.0, 62.0, 22.0],
                "id": "obj-316",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "array.some",
                "numoutlets": 3,
                "outlettype": ["int", "", "int"],
                "patching_rect": [1180.0, 410.0, 68.0, 22.0],
                "id": "obj-317",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "array.sort",
                "numoutlets": 3,
                "outlettype": ["", "", ""],
                "patching_rect": [1260.0, 410.0, 58.0, 22.0],
                "id": "obj-318",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "array.split",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [1340.0, 410.0, 60.0, 22.0],
                "id": "obj-319",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "array.stream",
                "numoutlets": 2,
                "outlettype": ["", "int"],
                "patching_rect": [1420.0, 410.0, 75.0, 22.0],
                "id": "obj-320",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "array.subarray",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [1500.0, 410.0, 85.0, 22.0],
                "id": "obj-321",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "array.thin",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [1580.0, 410.0, 58.0, 22.0],
                "id": "obj-322",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "array.tobuffer",
                "numoutlets": 0,
                "patching_rect": [60.0, 435.0, 79.0, 22.0],
                "id": "obj-323",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "array.tolist",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [140.0, 435.0, 63.0, 22.0],
                "id": "obj-324",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "array.tuplewise",
                "numoutlets": 2,
                "outlettype": ["", "int"],
                "patching_rect": [220.0, 435.0, 88.0, 22.0],
                "id": "obj-325",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "array.union",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [300.0, 435.0, 68.0, 22.0],
                "id": "obj-326",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "array.unique",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [380.0, 435.0, 74.0, 22.0],
                "id": "obj-327",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "array.unshift",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [460.0, 435.0, 74.0, 22.0],
                "id": "obj-328",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "array.wrap",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [540.0, 435.0, 64.0, 22.0],
                "id": "obj-329",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "asin",
                "numoutlets": 1,
                "outlettype": ["float"],
                "patching_rect": [620.0, 435.0, 31.0, 22.0],
                "id": "obj-330",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "asinh",
                "numoutlets": 1,
                "outlettype": ["float"],
                "patching_rect": [700.0, 435.0, 37.0, 22.0],
                "id": "obj-331",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "atan",
                "numoutlets": 1,
                "outlettype": ["float"],
                "patching_rect": [780.0, 435.0, 32.0, 22.0],
                "id": "obj-332",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "atan2",
                "numoutlets": 1,
                "outlettype": ["float"],
                "patching_rect": [860.0, 435.0, 39.0, 22.0],
                "id": "obj-333",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "atanh",
                "numoutlets": 1,
                "outlettype": ["float"],
                "patching_rect": [940.0, 435.0, 39.0, 22.0],
                "id": "obj-334",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "atodb",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [1020.0, 435.0, 39.0, 22.0],
                "id": "obj-335",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "atoi",
                "numoutlets": 1,
                "outlettype": ["list"],
                "patching_rect": [1100.0, 435.0, 28.0, 22.0],
                "id": "obj-336",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "attrui",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [1180.0, 435.0, 150.0, 22.0],
                "id": "obj-338",
                "numinlets": 1,
                "parameter_enable": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "varname": "u490011384",
                "text": "autopattr",
                "numoutlets": 4,
                "outlettype": ["", "", "", ""],
                "patching_rect": [1260.0, 435.0, 56.0, 22.0],
                "id": "obj-339",
                "numinlets": 1,
                "restore": {
                    "live.button": [0.0],
                    "live.dial": [0.0],
                    "live.drop": [""],
                    "live.gain~": [0.0],
                    "live.grid": [
                        0,
                        16,
                        16,
                        0,
                        16,
                        0,
                        1001,
                        2002,
                        3003,
                        4004,
                        5005,
                        6006,
                        7007,
                        8008,
                        9009,
                        10010,
                        11011,
                        12012,
                        13013,
                        14014,
                        15015,
                        2,
                        2,
                        2,
                        2,
                        2,
                        2,
                        2,
                        2,
                        2,
                        2,
                        2,
                        2,
                        2,
                        2,
                        2,
                        2,
                    ],
                    "live.menu": [0.0],
                    "live.numbox": [0.0],
                    "live.slider": [0.0],
                    "live.step": [
                        1,
                        16,
                        0,
                        1,
                        12,
                        0,
                        16,
                        59.0,
                        80.0,
                        0,
                        0,
                        60,
                        101,
                        4,
                        127,
                        127,
                        63,
                        83,
                        4,
                        127,
                        127,
                        67,
                        57,
                        4,
                        127,
                        127,
                        74,
                        78,
                        4,
                        127,
                        127,
                        70,
                        35,
                        4,
                        127,
                        127,
                        67,
                        75,
                        4,
                        127,
                        127,
                        60,
                        114,
                        4,
                        127,
                        127,
                        70,
                        75,
                        4,
                        127,
                        127,
                        67,
                        59,
                        4,
                        127,
                        127,
                        79,
                        80,
                        4,
                        127,
                        127,
                        60,
                        100,
                        4,
                        127,
                        127,
                        70,
                        84,
                        4,
                        127,
                        127,
                        60,
                        114,
                        4,
                        127,
                        127,
                        63,
                        98,
                        4,
                        127,
                        127,
                        70,
                        97,
                        4,
                        127,
                        127,
                        62,
                        103,
                        4,
                        127,
                        127,
                    ],
                    "live.tab": [0.0],
                    "live.text": [0.0],
                    "live.toggle": [0.0],
                    "mc.live.gain~": [0.0],
                },
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "bag",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [1340.0, 435.0, 29.0, 22.0],
                "id": "obj-340",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "bangbang",
                "numoutlets": 2,
                "outlettype": ["bang", "bang"],
                "patching_rect": [1420.0, 435.0, 62.0, 22.0],
                "id": "obj-341",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "bendin",
                "numoutlets": 2,
                "outlettype": ["int", "int"],
                "patching_rect": [1500.0, 435.0, 45.0, 22.0],
                "id": "obj-342",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "bendout",
                "numoutlets": 0,
                "patching_rect": [1580.0, 435.0, 52.0, 22.0],
                "id": "obj-343",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "bitand",
                "numoutlets": 0,
                "patching_rect": [60.0, 460.0, 41.0, 22.0],
                "id": "obj-344",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "bitor",
                "numoutlets": 0,
                "patching_rect": [140.0, 460.0, 32.0, 22.0],
                "id": "obj-345",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "bline",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [220.0, 460.0, 34.0, 22.0],
                "id": "obj-346",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "bondo",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [300.0, 460.0, 42.0, 22.0],
                "id": "obj-347",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "borax",
                "numoutlets": 9,
                "outlettype": [
                    "int",
                    "int",
                    "int",
                    "int",
                    "int",
                    "int",
                    "int",
                    "int",
                    "int",
                ],
                "patching_rect": [380.0, 460.0, 39.0, 22.0],
                "id": "obj-348",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "bpatcher",
                "viewvisibility": 1,
                "offset": [0.0, 0.0],
                "lockeddragscroll": 0,
                "clickthrough": 0,
                "enablehscroll": 0,
                "enablevscroll": 0,
                "lockedsize": 0,
                "bgmode": 0,
                "border": 0,
                "numoutlets": 0,
                "patching_rect": [460.0, 460.0, 128.0, 128.0],
                "id": "obj-350",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "bucket",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [540.0, 460.0, 44.0, 22.0],
                "id": "obj-351",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "buddy",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [620.0, 460.0, 41.0, 22.0],
                "id": "obj-352",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "button",
                "numoutlets": 1,
                "outlettype": ["bang"],
                "patching_rect": [700.0, 460.0, 24.0, 24.0],
                "id": "obj-354",
                "numinlets": 1,
                "parameter_enable": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "capture",
                "numoutlets": 2,
                "outlettype": ["", "int"],
                "patching_rect": [780.0, 460.0, 49.0, 22.0],
                "id": "obj-355",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "cartopol",
                "numoutlets": 2,
                "outlettype": ["float", "float"],
                "patching_rect": [860.0, 460.0, 51.0, 22.0],
                "id": "obj-356",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "change",
                "numoutlets": 3,
                "outlettype": ["", "int", "int"],
                "patching_rect": [940.0, 460.0, 48.0, 22.0],
                "id": "obj-357",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "chooser",
                "numoutlets": 6,
                "items": "<empty>",
                "fontface": 0,
                "outlettype": ["", "", "", "", "", ""],
                "patching_rect": [1020.0, 460.0, 100.0, 100.0],
                "id": "obj-359",
                "fontsize": 12.0,
                "numinlets": 1,
                "parameter_enable": 0,
                "fontname": "Arial",
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "clip",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [1100.0, 460.0, 27.0, 22.0],
                "id": "obj-360",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "clocker",
                "numoutlets": 1,
                "outlettype": ["float"],
                "patching_rect": [1180.0, 460.0, 47.0, 22.0],
                "id": "obj-361",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "closebang",
                "numoutlets": 1,
                "outlettype": ["bang"],
                "patching_rect": [1260.0, 460.0, 63.0, 22.0],
                "id": "obj-362",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "coll",
                "numoutlets": 4,
                "outlettype": ["", "", "", ""],
                "patching_rect": [1340.0, 460.0, 27.0, 22.0],
                "id": "obj-363",
                "numinlets": 1,
                "saved_object_attributes": {"embed": 0, "precision": 6},
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "colorpicker",
                "numoutlets": 2,
                "outlettype": ["list", "bang"],
                "patching_rect": [1420.0, 460.0, 67.0, 22.0],
                "id": "obj-364",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "combine",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [1500.0, 460.0, 54.0, 22.0],
                "id": "obj-365",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "comment",
                "numoutlets": 0,
                "patching_rect": [1580.0, 460.0, 150.0, 20.0],
                "id": "obj-367",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "conformpath",
                "numoutlets": 2,
                "outlettype": ["", "int"],
                "patching_rect": [60.0, 485.0, 75.0, 22.0],
                "id": "obj-368",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "console",
                "numoutlets": 3,
                "outlettype": ["", "", "int"],
                "patching_rect": [140.0, 485.0, 50.0, 22.0],
                "id": "obj-369",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "cos",
                "numoutlets": 1,
                "outlettype": ["float"],
                "patching_rect": [220.0, 485.0, 27.0, 22.0],
                "id": "obj-370",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "cosh",
                "numoutlets": 1,
                "outlettype": ["float"],
                "patching_rect": [300.0, 485.0, 34.0, 22.0],
                "id": "obj-371",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "counter",
                "numoutlets": 4,
                "outlettype": ["int", "", "", "int"],
                "patching_rect": [380.0, 485.0, 49.0, 22.0],
                "id": "obj-372",
                "numinlets": 5,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "cpuclock",
                "numoutlets": 1,
                "outlettype": ["float"],
                "patching_rect": [460.0, 485.0, 55.0, 22.0],
                "id": "obj-373",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "crosspatch",
                "dividers": "none",
                "numoutlets": 2,
                "incolormap": "none",
                "fontface": 0,
                "outlettype": ["", "dictionary"],
                "patching_rect": [540.0, 485.0, 280.0, 80.0],
                "id": "obj-375",
                "fontsize": 12.0,
                "outcolormap": "none",
                "numinlets": 1,
                "parameter_enable": 0,
                "fontname": "Arial",
                "numins": 4,
                "numouts": 4,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "ctlin",
                "numoutlets": 3,
                "outlettype": ["int", "int", "int"],
                "patching_rect": [620.0, 485.0, 30.0, 22.0],
                "id": "obj-376",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "ctlout",
                "numoutlets": 0,
                "patching_rect": [700.0, 485.0, 37.0, 22.0],
                "id": "obj-377",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "cycle",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [780.0, 485.0, 36.0, 22.0],
                "id": "obj-378",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "date",
                "numoutlets": 3,
                "outlettype": ["list", "list", "int"],
                "patching_rect": [860.0, 485.0, 32.0, 22.0],
                "id": "obj-379",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "dbtoa",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [940.0, 485.0, 39.0, 22.0],
                "id": "obj-380",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "decide",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [1020.0, 485.0, 44.0, 22.0],
                "id": "obj-381",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "decode",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [1100.0, 485.0, 48.0, 22.0],
                "id": "obj-382",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "defer",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [1180.0, 485.0, 36.0, 22.0],
                "id": "obj-383",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "deferlow",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [1260.0, 485.0, 54.0, 22.0],
                "id": "obj-384",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "delay",
                "numoutlets": 1,
                "outlettype": ["bang"],
                "patching_rect": [1340.0, 485.0, 37.0, 22.0],
                "id": "obj-385",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "detonate",
                "numoutlets": 8,
                "outlettype": ["int", "int", "int", "int", "int", "int", "int", "int"],
                "patching_rect": [1420.0, 485.0, 55.0, 22.0],
                "id": "obj-386",
                "numinlets": 8,
                "save": [
                    "#N",
                    "detonate",
                    "u172011514",
                    ";",
                    "#X",
                    "setparam",
                    0,
                    "Time",
                    0,
                    0,
                    999999,
                    0,
                    1000,
                    200,
                    0,
                    ";",
                    "#X",
                    "setparam",
                    1,
                    "Pitch",
                    0,
                    0,
                    127,
                    60,
                    12,
                    4,
                    0,
                    ";",
                    "#X",
                    "setparam",
                    2,
                    "Vel",
                    0,
                    0,
                    127,
                    64,
                    12,
                    4,
                    0,
                    ";",
                    "#X",
                    "setparam",
                    3,
                    "Dur",
                    0,
                    1,
                    99999,
                    200,
                    800,
                    200,
                    0,
                    ";",
                    "#X",
                    "setparam",
                    4,
                    "Chan",
                    0,
                    1,
                    16,
                    1,
                    8,
                    1,
                    0,
                    ";",
                    "#X",
                    "setparam",
                    5,
                    "Track",
                    0,
                    1,
                    32,
                    1,
                    8,
                    1,
                    0,
                    ";",
                    "#X",
                    "setparam",
                    6,
                    "X1",
                    0,
                    0,
                    999,
                    0,
                    80,
                    20,
                    0,
                    ";",
                    "#X",
                    "setparam",
                    7,
                    "X2",
                    0,
                    0,
                    999,
                    0,
                    80,
                    20,
                    0,
                    ";",
                    "#X",
                    "restore",
                    ";",
                    "#X",
                    "stop",
                    ";",
                ],
            }
        },
        {
            "box": {
                "maxclass": "dial",
                "numoutlets": 1,
                "outlettype": ["float"],
                "patching_rect": [1500.0, 485.0, 40.0, 40.0],
                "id": "obj-388",
                "numinlets": 1,
                "parameter_enable": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "dialog",
                "numoutlets": 3,
                "outlettype": ["", "bang", "bang"],
                "patching_rect": [1580.0, 485.0, 41.0, 22.0],
                "id": "obj-389",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "dict.compare",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [60.0, 510.0, 77.0, 22.0],
                "id": "obj-390",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "dict.deserialize",
                "numoutlets": 1,
                "outlettype": ["dictionary"],
                "patching_rect": [140.0, 510.0, 88.0, 22.0],
                "id": "obj-391",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "dict.group",
                "numoutlets": 1,
                "outlettype": ["dictionary"],
                "patching_rect": [220.0, 510.0, 61.0, 22.0],
                "id": "obj-392",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "dict.iter",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [300.0, 510.0, 47.0, 22.0],
                "id": "obj-393",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "dict.join",
                "numoutlets": 1,
                "outlettype": ["dictionary"],
                "patching_rect": [380.0, 510.0, 49.0, 22.0],
                "id": "obj-394",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "dict",
                "numoutlets": 5,
                "outlettype": ["dictionary", "", "", "", ""],
                "patching_rect": [460.0, 510.0, 27.0, 22.0],
                "id": "obj-395",
                "numinlets": 2,
                "saved_object_attributes": {
                    "embed": 0,
                    "legacy": 0,
                    "parameter_enable": 0,
                    "parameter_mappable": 0,
                },
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "dict.pack",
                "numoutlets": 1,
                "outlettype": ["dictionary"],
                "patching_rect": [540.0, 510.0, 56.0, 22.0],
                "id": "obj-396",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "dict.print",
                "numoutlets": 0,
                "patching_rect": [620.0, 510.0, 54.0, 22.0],
                "id": "obj-397",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "dict.route",
                "numoutlets": 2,
                "outlettype": ["dictionary", "dictionary"],
                "patching_rect": [700.0, 510.0, 58.0, 22.0],
                "id": "obj-398",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "dict.serialize",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [780.0, 510.0, 75.0, 22.0],
                "id": "obj-399",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "dict.slice",
                "numoutlets": 2,
                "outlettype": ["dictionary", "dictionary"],
                "patching_rect": [860.0, 510.0, 55.0, 22.0],
                "id": "obj-400",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "dict.strip",
                "numoutlets": 2,
                "outlettype": ["dictionary", ""],
                "patching_rect": [940.0, 510.0, 53.0, 22.0],
                "id": "obj-401",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "dict.unpack",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [1020.0, 510.0, 69.0, 22.0],
                "id": "obj-402",
                "numinlets": 1,
                "saved_object_attributes": {"legacy": 0},
            }
        },
        {
            "box": {
                "maxclass": "dict.view",
                "numoutlets": 0,
                "patching_rect": [1100.0, 510.0, 100.0, 100.0],
                "id": "obj-404",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "div",
                "numoutlets": 0,
                "patching_rect": [1180.0, 510.0, 24.0, 22.0],
                "id": "obj-405",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "dropfile",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [1260.0, 510.0, 33.0, 42.0],
                "id": "obj-407",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "drunk",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [1340.0, 510.0, 39.0, 22.0],
                "id": "obj-408",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "dsp",
                "numoutlets": 0,
                "patching_rect": [1420.0, 510.0, 28.0, 22.0],
                "id": "obj-409",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "equals",
                "numoutlets": 0,
                "patching_rect": [1500.0, 510.0, 44.0, 22.0],
                "id": "obj-410",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "error",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [1580.0, 510.0, 34.0, 22.0],
                "id": "obj-411",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "expr",
                "numoutlets": 0,
                "patching_rect": [60.0, 535.0, 32.0, 22.0],
                "id": "obj-412",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "filedate",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [140.0, 535.0, 47.0, 22.0],
                "id": "obj-413",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "filein",
                "numoutlets": 3,
                "outlettype": ["int", "bang", "bang"],
                "patching_rect": [220.0, 535.0, 33.0, 22.0],
                "id": "obj-414",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "filepath",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [300.0, 535.0, 47.0, 22.0],
                "id": "obj-415",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "filewatch",
                "numoutlets": 1,
                "outlettype": ["bang"],
                "patching_rect": [380.0, 535.0, 55.0, 22.0],
                "id": "obj-416",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "flonum",
                "numoutlets": 2,
                "format": 6,
                "outlettype": ["", "bang"],
                "patching_rect": [540.0, 535.0, 50.0, 22.0],
                "id": "obj-418",
                "numinlets": 1,
                "parameter_enable": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "flush",
                "numoutlets": 2,
                "outlettype": ["int", "int"],
                "patching_rect": [620.0, 535.0, 34.0, 22.0],
                "id": "obj-419",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "folder",
                "numoutlets": 2,
                "outlettype": ["", "int"],
                "patching_rect": [700.0, 535.0, 39.0, 22.0],
                "id": "obj-420",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "follow",
                "numoutlets": 2,
                "outlettype": ["int", "int"],
                "patching_rect": [780.0, 535.0, 39.0, 22.0],
                "id": "obj-421",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "fontlist",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [860.0, 535.0, 43.0, 22.0],
                "id": "obj-422",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "forward",
                "numoutlets": 0,
                "patching_rect": [940.0, 535.0, 49.0, 22.0],
                "id": "obj-423",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "fpic",
                "numoutlets": 1,
                "outlettype": ["jit_matrix"],
                "patching_rect": [1020.0, 535.0, 100.0, 50.0],
                "id": "obj-425",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "freebang",
                "numoutlets": 1,
                "outlettype": ["bang"],
                "patching_rect": [1100.0, 535.0, 56.0, 22.0],
                "id": "obj-426",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "fromsymbol",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [1180.0, 535.0, 71.0, 22.0],
                "id": "obj-427",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "fswap",
                "numoutlets": 2,
                "outlettype": ["int", "int"],
                "patching_rect": [1260.0, 535.0, 40.0, 22.0],
                "id": "obj-428",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "ftom",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [1340.0, 535.0, 32.0, 22.0],
                "id": "obj-429",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "funbuff",
                "numoutlets": 3,
                "outlettype": ["int", "int", "bang"],
                "patching_rect": [1420.0, 535.0, 45.0, 22.0],
                "id": "obj-430",
                "numinlets": 2,
                "save": ["#N", "funbuff", 0, ";"],
            }
        },
        {
            "box": {
                "maxclass": "function",
                "numoutlets": 4,
                "outlettype": ["float", "", "", "bang"],
                "classic_curve": 0,
                "patching_rect": [1500.0, 535.0, 200.0, 100.0],
                "id": "obj-432",
                "numinlets": 1,
                "parameter_enable": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "funnel",
                "numoutlets": 1,
                "outlettype": ["list"],
                "patching_rect": [1580.0, 535.0, 41.0, 22.0],
                "id": "obj-433",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "gate",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [60.0, 560.0, 32.0, 22.0],
                "id": "obj-434",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "gestalt",
                "numoutlets": 2,
                "outlettype": ["", "int"],
                "patching_rect": [140.0, 560.0, 44.0, 22.0],
                "id": "obj-435",
                "numinlets": 1,
                "saved_object_attributes": {"selector": ""},
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "getattr",
                "numoutlets": 3,
                "outlettype": ["", "", ""],
                "patching_rect": [220.0, 560.0, 43.0, 22.0],
                "id": "obj-436",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "grab",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [300.0, 560.0, 33.0, 22.0],
                "id": "obj-437",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "greaterthan",
                "numoutlets": 0,
                "patching_rect": [380.0, 560.0, 70.0, 22.0],
                "id": "obj-438",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "greaterthaneq",
                "numoutlets": 0,
                "patching_rect": [460.0, 560.0, 83.0, 22.0],
                "id": "obj-439",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "gswitch",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [540.0, 560.0, 41.0, 32.0],
                "id": "obj-441",
                "numinlets": 3,
                "parameter_enable": 0,
            }
        },
        {
            "box": {
                "maxclass": "gswitch2",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [620.0, 560.0, 39.0, 32.0],
                "id": "obj-443",
                "numinlets": 2,
                "parameter_enable": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "hi",
                "numoutlets": 2,
                "outlettype": ["list", ""],
                "patching_rect": [700.0, 560.0, 18.0, 22.0],
                "id": "obj-444",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "histo",
                "numoutlets": 2,
                "outlettype": ["int", "int"],
                "patching_rect": [860.0, 560.0, 34.0, 22.0],
                "id": "obj-445",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "hover",
                "numoutlets": 4,
                "outlettype": ["", "", "", ""],
                "patching_rect": [940.0, 560.0, 39.0, 22.0],
                "id": "obj-446",
                "numinlets": 1,
                "saved_object_attributes": {"mode": 0},
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "if",
                "numoutlets": 0,
                "patching_rect": [1020.0, 560.0, 18.0, 22.0],
                "id": "obj-447",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "i",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [1100.0, 560.0, 18.0, 22.0],
                "id": "obj-448",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "imovie",
                "numoutlets": 3,
                "name": "",
                "outlettype": ["int", "int", "int"],
                "patching_rect": [1180.0, 560.0, 320.0, 240.0],
                "id": "obj-450",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "incdec",
                "numoutlets": 1,
                "outlettype": ["float"],
                "patching_rect": [1260.0, 560.0, 20.0, 24.0],
                "id": "obj-452",
                "numinlets": 1,
                "parameter_enable": 0,
            }
        },
        {
            "box": {
                "maxclass": "itable",
                "numoutlets": 2,
                "size": 128,
                "name": "",
                "range": 128,
                "outlettype": ["int", "bang"],
                "patching_rect": [1420.0, 560.0, 160.0, 145.0],
                "id": "obj-454",
                "numinlets": 2,
                "parameter_enable": 0,
                "table_data": [
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                ],
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "iter",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [1500.0, 560.0, 25.0, 22.0],
                "id": "obj-455",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "itoa",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [1580.0, 560.0, 28.0, 22.0],
                "id": "obj-456",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jbox",
                "numoutlets": 0,
                "patching_rect": [60.0, 585.0, 31.0, 22.0],
                "id": "obj-457",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "jit.cellblock",
                "numoutlets": 4,
                "fontface": 0,
                "outlettype": ["list", "", "", ""],
                "patching_rect": [140.0, 585.0, 200.0, 200.0],
                "id": "obj-459",
                "fontsize": 12.0,
                "numinlets": 2,
                "fontname": "Arial",
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit_kernel",
                "numoutlets": 0,
                "patching_rect": [220.0, 585.0, 57.0, 22.0],
                "id": "obj-460",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "join",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [300.0, 585.0, 27.0, 22.0],
                "id": "obj-461",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "js",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [380.0, 585.0, 18.0, 22.0],
                "id": "obj-462",
                "numinlets": 1,
                "saved_object_attributes": {"filename": "", "parameter_enable": 0},
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jstrigger",
                "numoutlets": 0,
                "patching_rect": [460.0, 585.0, 51.0, 22.0],
                "id": "obj-463",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "jsui",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [540.0, 585.0, 64.0, 64.0],
                "id": "obj-465",
                "numinlets": 1,
                "parameter_enable": 0,
            }
        },
        {
            "box": {
                "maxclass": "jweb",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [620.0, 585.0, 320.0, 240.0],
                "id": "obj-467",
                "rendermode": 0,
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "key",
                "numoutlets": 4,
                "outlettype": ["int", "int", "int", "int"],
                "patching_rect": [700.0, 585.0, 27.0, 22.0],
                "id": "obj-468",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "keyup",
                "numoutlets": 4,
                "outlettype": ["int", "int", "int", "int"],
                "patching_rect": [780.0, 585.0, 41.0, 22.0],
                "id": "obj-469",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "kslider",
                "numoutlets": 2,
                "outlettype": ["int", "int"],
                "patching_rect": [860.0, 585.0, 336.0, 53.0],
                "id": "obj-471",
                "numinlets": 2,
                "parameter_enable": 0,
            }
        },
        {
            "box": {
                "maxclass": "lcd",
                "numoutlets": 4,
                "outlettype": ["list", "list", "int", ""],
                "patching_rect": [940.0, 585.0, 128.0, 128.0],
                "id": "obj-473",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "led",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [1020.0, 585.0, 24.0, 24.0],
                "id": "obj-475",
                "numinlets": 1,
                "parameter_enable": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "lessthan",
                "numoutlets": 0,
                "patching_rect": [1100.0, 585.0, 53.0, 22.0],
                "id": "obj-476",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "lessthaneq",
                "numoutlets": 0,
                "patching_rect": [1180.0, 585.0, 67.0, 22.0],
                "id": "obj-477",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "line",
                "numoutlets": 2,
                "outlettype": ["", "bang"],
                "patching_rect": [1260.0, 585.0, 27.0, 22.0],
                "id": "obj-478",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "linedrive",
                "numoutlets": 0,
                "patching_rect": [1340.0, 585.0, 53.0, 22.0],
                "id": "obj-479",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "listfunnel",
                "numoutlets": 1,
                "outlettype": ["list"],
                "patching_rect": [1420.0, 585.0, 56.0, 22.0],
                "id": "obj-480",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "loadbang",
                "numoutlets": 1,
                "outlettype": ["bang"],
                "patching_rect": [1500.0, 585.0, 58.0, 22.0],
                "id": "obj-481",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "loadmess",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [1580.0, 585.0, 60.0, 22.0],
                "id": "obj-482",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "logand",
                "numoutlets": 0,
                "patching_rect": [60.0, 610.0, 45.0, 22.0],
                "id": "obj-483",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "logor",
                "numoutlets": 0,
                "patching_rect": [140.0, 610.0, 35.0, 22.0],
                "id": "obj-484",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "makenote",
                "numoutlets": 2,
                "outlettype": ["float", "float"],
                "patching_rect": [220.0, 610.0, 61.0, 22.0],
                "id": "obj-485",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mappings",
                "numoutlets": 0,
                "patching_rect": [300.0, 610.0, 61.0, 22.0],
                "id": "obj-486",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "match",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [380.0, 610.0, 41.0, 22.0],
                "id": "obj-487",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "matrix",
                "numoutlets": 3,
                "outlettype": ["dictionary", "", ""],
                "patching_rect": [460.0, 610.0, 41.0, 22.0],
                "id": "obj-488",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "matrixctrl",
                "numoutlets": 2,
                "outlettype": ["list", "list"],
                "patching_rect": [540.0, 610.0, 130.0, 66.0],
                "id": "obj-490",
                "numinlets": 1,
                "parameter_enable": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "max",
                "numoutlets": 0,
                "patching_rect": [620.0, 610.0, 31.0, 22.0],
                "id": "obj-491",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "maximum",
                "numoutlets": 2,
                "outlettype": ["int", "int"],
                "patching_rect": [700.0, 610.0, 61.0, 22.0],
                "id": "obj-492",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "maxurl",
                "numoutlets": 2,
                "outlettype": ["dictionary", ""],
                "patching_rect": [780.0, 610.0, 45.0, 22.0],
                "id": "obj-493",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "mc.function",
                "numoutlets": 5,
                "outlettype": ["float", "", "", "bang", "int"],
                "classic_curve": 0,
                "patching_rect": [860.0, 610.0, 200.0, 118.0],
                "id": "obj-495",
                "numinlets": 1,
                "parameter_enable": 0,
                "data": [{}],
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.getattr",
                "numoutlets": 4,
                "outlettype": ["", "", "", ""],
                "patching_rect": [940.0, 610.0, 62.0, 22.0],
                "id": "obj-496",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.line",
                "numoutlets": 3,
                "outlettype": ["", "", ""],
                "patching_rect": [1020.0, 610.0, 47.0, 22.0],
                "id": "obj-497",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mean",
                "numoutlets": 2,
                "outlettype": ["float", "int"],
                "patching_rect": [1100.0, 610.0, 39.0, 22.0],
                "id": "obj-498",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "menubar",
                "numoutlets": 4,
                "outlettype": ["int", "int", "int", "int"],
                "patching_rect": [1180.0, 610.0, 56.0, 22.0],
                "id": "obj-499",
                "numinlets": 1,
                "save": [
                    "#N",
                    "menubar",
                    4,
                    0,
                    ";",
                    "#X",
                    "about",
                    "About",
                    "Max",
                    ";",
                    "#X",
                    "closeitem",
                    ";",
                    "#X",
                    "end",
                    ";",
                ],
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "metro",
                "numoutlets": 1,
                "outlettype": ["bang"],
                "patching_rect": [1260.0, 610.0, 39.0, 22.0],
                "id": "obj-500",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "midiflush",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [1340.0, 610.0, 56.0, 22.0],
                "id": "obj-501",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "midiformat",
                "numoutlets": 2,
                "outlettype": ["int", ""],
                "patching_rect": [1420.0, 610.0, 65.0, 22.0],
                "id": "obj-502",
                "numinlets": 7,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "midiin",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [1500.0, 610.0, 40.0, 22.0],
                "id": "obj-503",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "midiinfo",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [1580.0, 610.0, 50.0, 22.0],
                "id": "obj-504",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "midiout",
                "numoutlets": 0,
                "patching_rect": [60.0, 635.0, 47.0, 22.0],
                "id": "obj-505",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "midiparse",
                "numoutlets": 8,
                "outlettype": ["", "", "", "int", "int", "", "int", ""],
                "patching_rect": [140.0, 635.0, 61.0, 22.0],
                "id": "obj-506",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "minimum",
                "numoutlets": 2,
                "outlettype": ["int", "int"],
                "patching_rect": [220.0, 635.0, 57.0, 22.0],
                "id": "obj-507",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "minus",
                "numoutlets": 0,
                "patching_rect": [300.0, 635.0, 41.0, 22.0],
                "id": "obj-508",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "modifiers",
                "numoutlets": 5,
                "outlettype": ["int", "int", "int", "int", "int"],
                "patching_rect": [380.0, 635.0, 57.0, 22.0],
                "id": "obj-509",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "modulo",
                "numoutlets": 0,
                "patching_rect": [460.0, 635.0, 48.0, 22.0],
                "id": "obj-510",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mousefilter",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [540.0, 635.0, 67.0, 22.0],
                "id": "obj-511",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mousestate",
                "numoutlets": 5,
                "outlettype": ["int", "int", "int", "int", "int"],
                "patching_rect": [620.0, 635.0, 71.0, 22.0],
                "id": "obj-512",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "movie",
                "numoutlets": 3,
                "outlettype": ["int", "int", "int"],
                "patching_rect": [700.0, 635.0, 41.0, 22.0],
                "id": "obj-513",
                "numinlets": 1,
                "saved_object_attributes": {"name": ""},
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mpeconfig",
                "numoutlets": 2,
                "outlettype": ["int", "mpeevent"],
                "patching_rect": [780.0, 635.0, 64.0, 22.0],
                "id": "obj-514",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mpeformat",
                "numoutlets": 2,
                "outlettype": ["int", "mpeevent"],
                "patching_rect": [860.0, 635.0, 66.0, 22.0],
                "id": "obj-515",
                "numinlets": 16,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mpeparse",
                "numoutlets": 10,
                "outlettype": ["", "", "", "", "int", "", "int", "int", "int", ""],
                "patching_rect": [940.0, 635.0, 62.0, 22.0],
                "id": "obj-516",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mtof",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [1020.0, 635.0, 32.0, 22.0],
                "id": "obj-517",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mtr",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [1100.0, 635.0, 26.0, 22.0],
                "id": "obj-518",
                "numinlets": 2,
                "saved_object_attributes": {"embed": 0},
            }
        },
        {
            "box": {
                "maxclass": "multirange",
                "numoutlets": 4,
                "outlettype": ["float", "", "", "bang"],
                "patching_rect": [1180.0, 635.0, 200.0, 100.0],
                "id": "obj-520",
                "numinlets": 1,
                "parameter_enable": 0,
            }
        },
        {
            "box": {
                "maxclass": "multislider",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [1260.0, 635.0, 20.0, 140.0],
                "id": "obj-522",
                "numinlets": 1,
                "parameter_enable": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mxj",
                "numoutlets": 0,
                "patching_rect": [1340.0, 635.0, 27.0, 22.0],
                "id": "obj-523",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "next",
                "numoutlets": 2,
                "outlettype": ["bang", "bang"],
                "patching_rect": [1420.0, 635.0, 31.0, 22.0],
                "id": "obj-524",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "nodes",
                "nsize": [0.2],
                "numoutlets": 3,
                "xplace": [0.083333333333333],
                "outlettype": ["", "", ""],
                "nodesnames": ["1"],
                "patching_rect": [1500.0, 635.0, 100.0, 100.0],
                "id": "obj-526",
                "yplace": [0.083333333333333],
                "numinlets": 1,
                "parameter_enable": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "notein",
                "numoutlets": 3,
                "outlettype": ["int", "int", "int"],
                "patching_rect": [1580.0, 635.0, 41.0, 22.0],
                "id": "obj-527",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "noteout",
                "numoutlets": 0,
                "patching_rect": [60.0, 660.0, 49.0, 22.0],
                "id": "obj-528",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "notequals",
                "numoutlets": 0,
                "patching_rect": [140.0, 660.0, 61.0, 22.0],
                "id": "obj-529",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "nrpnin",
                "numoutlets": 4,
                "outlettype": ["int", "int", "int", "int"],
                "patching_rect": [220.0, 660.0, 42.0, 22.0],
                "id": "obj-530",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "nrpnout",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [300.0, 660.0, 49.0, 22.0],
                "id": "obj-531",
                "numinlets": 4,
            }
        },
        {
            "box": {
                "maxclass": "nslider",
                "numoutlets": 2,
                "outlettype": ["int", "int"],
                "patching_rect": [380.0, 660.0, 75.0, 198.0],
                "id": "obj-533",
                "numinlets": 2,
                "parameter_enable": 0,
            }
        },
        {
            "box": {
                "maxclass": "number",
                "numoutlets": 2,
                "outlettype": ["", "bang"],
                "patching_rect": [460.0, 660.0, 50.0, 22.0],
                "id": "obj-535",
                "numinlets": 1,
                "parameter_enable": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "numkey",
                "numoutlets": 2,
                "outlettype": ["int", "int"],
                "patching_rect": [540.0, 660.0, 51.0, 22.0],
                "id": "obj-536",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "offer",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [620.0, 660.0, 32.0, 22.0],
                "id": "obj-537",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "onebang",
                "numoutlets": 2,
                "outlettype": ["bang", "bang"],
                "patching_rect": [700.0, 660.0, 55.0, 22.0],
                "id": "obj-538",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "onecopy",
                "numoutlets": 0,
                "patching_rect": [780.0, 660.0, 54.0, 22.0],
                "id": "obj-539",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "opendialog",
                "numoutlets": 2,
                "outlettype": ["", "bang"],
                "patching_rect": [860.0, 660.0, 67.0, 22.0],
                "id": "obj-540",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "pack",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [940.0, 660.0, 34.0, 22.0],
                "id": "obj-541",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "pak",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [1020.0, 660.0, 28.0, 22.0],
                "id": "obj-542",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "panel",
                "numoutlets": 0,
                "patching_rect": [1100.0, 660.0, 128.0, 128.0],
                "id": "obj-544",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "past",
                "numoutlets": 1,
                "outlettype": ["bang"],
                "patching_rect": [1180.0, 660.0, 31.0, 22.0],
                "id": "obj-545",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "patcherargs",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [1260.0, 660.0, 72.0, 22.0],
                "id": "obj-546",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "varname": "u038012005",
                "text": "pattr",
                "numoutlets": 3,
                "outlettype": ["", "", ""],
                "patching_rect": [1340.0, 660.0, 33.0, 22.0],
                "id": "obj-547",
                "numinlets": 1,
                "restore": [0],
                "saved_object_attributes": {
                    "parameter_enable": 0,
                    "parameter_mappable": 0,
                },
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "pattrforward",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [1420.0, 660.0, 73.0, 22.0],
                "id": "obj-548",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "pattrhub",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [1500.0, 660.0, 53.0, 22.0],
                "id": "obj-549",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "pattrmarker",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [1580.0, 660.0, 70.0, 22.0],
                "id": "obj-550",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "varname": "u252012023",
                "text": "pattrstorage",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [60.0, 685.0, 73.0, 22.0],
                "id": "obj-551",
                "numinlets": 1,
                "saved_object_attributes": {
                    "client_rect": [100, 100, 500, 600],
                    "parameter_enable": 0,
                    "parameter_mappable": 0,
                    "storage_rect": [200, 200, 800, 500],
                },
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "pcontrol",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [140.0, 685.0, 51.0, 22.0],
                "id": "obj-552",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "peak",
                "numoutlets": 3,
                "outlettype": ["int", "int", "int"],
                "patching_rect": [220.0, 685.0, 35.0, 22.0],
                "id": "obj-553",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "pgmin",
                "numoutlets": 2,
                "outlettype": ["int", "int"],
                "patching_rect": [300.0, 685.0, 41.0, 22.0],
                "id": "obj-554",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "pgmout",
                "numoutlets": 0,
                "patching_rect": [380.0, 685.0, 49.0, 22.0],
                "id": "obj-555",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "pictctrl",
                "clickedimage": 1,
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [460.0, 685.0, 20.0, 20.0],
                "id": "obj-557",
                "numinlets": 1,
                "parameter_enable": 0,
            }
        },
        {
            "box": {
                "maxclass": "pictslider",
                "numoutlets": 2,
                "outlettype": ["int", "int"],
                "patching_rect": [540.0, 685.0, 100.0, 100.0],
                "id": "obj-559",
                "numinlets": 2,
                "parameter_enable": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "pipe",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [620.0, 685.0, 31.0, 22.0],
                "id": "obj-560",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "playbar",
                "numoutlets": 2,
                "outlettype": ["", "int"],
                "patching_rect": [700.0, 685.0, 320.0, 16.0],
                "id": "obj-562",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "plus",
                "numoutlets": 0,
                "patching_rect": [780.0, 685.0, 31.0, 22.0],
                "id": "obj-563",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "poltocar",
                "numoutlets": 2,
                "outlettype": ["float", "float"],
                "patching_rect": [860.0, 685.0, 51.0, 22.0],
                "id": "obj-564",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "poly",
                "numoutlets": 4,
                "outlettype": ["int", "int", "int", "list"],
                "patching_rect": [940.0, 685.0, 31.0, 22.0],
                "id": "obj-565",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "polyin",
                "numoutlets": 3,
                "outlettype": ["int", "int", "int"],
                "patching_rect": [1020.0, 685.0, 40.0, 22.0],
                "id": "obj-566",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "polymidiin",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [1100.0, 685.0, 62.0, 22.0],
                "id": "obj-567",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "polyout",
                "numoutlets": 0,
                "patching_rect": [1180.0, 685.0, 47.0, 22.0],
                "id": "obj-568",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "pong",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [1260.0, 685.0, 35.0, 22.0],
                "id": "obj-569",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "pow",
                "numoutlets": 1,
                "outlettype": ["float"],
                "patching_rect": [1340.0, 685.0, 31.0, 22.0],
                "id": "obj-570",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "preset",
                "numoutlets": 5,
                "outlettype": ["preset", "int", "preset", "int", ""],
                "patching_rect": [1420.0, 685.0, 100.0, 40.0],
                "id": "obj-572",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "print",
                "numoutlets": 0,
                "patching_rect": [1500.0, 685.0, 32.0, 22.0],
                "id": "obj-573",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "prob",
                "numoutlets": 2,
                "outlettype": ["int", "bang"],
                "patching_rect": [1580.0, 685.0, 33.0, 22.0],
                "id": "obj-574",
                "numinlets": 1,
                "save": ["#N", "prob", ";"],
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "project",
                "numoutlets": 0,
                "patching_rect": [60.0, 710.0, 45.0, 22.0],
                "id": "obj-575",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "pv",
                "numoutlets": 0,
                "patching_rect": [140.0, 710.0, 21.0, 22.0],
                "id": "obj-576",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "pvar",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [220.0, 710.0, 32.0, 22.0],
                "id": "obj-577",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "qlim",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [300.0, 710.0, 31.0, 22.0],
                "id": "obj-578",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "qlist",
                "numoutlets": 3,
                "outlettype": ["", "bang", "bang"],
                "patching_rect": [380.0, 710.0, 30.0, 22.0],
                "id": "obj-579",
                "numinlets": 1,
                "save": ["#N", "qlist", ";"],
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "qmetro",
                "numoutlets": 1,
                "outlettype": ["bang"],
                "patching_rect": [460.0, 710.0, 46.0, 22.0],
                "id": "obj-580",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "quickthresh",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [540.0, 710.0, 70.0, 22.0],
                "id": "obj-581",
                "numinlets": 4,
            }
        },
        {
            "box": {
                "maxclass": "radiogroup",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [620.0, 710.0, 18.0, 34.0],
                "id": "obj-583",
                "numinlets": 1,
                "parameter_enable": 0,
                "itemtype": 0,
                "size": 2,
                "value": 0,
                "disabled": [0, 0],
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "random",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [700.0, 710.0, 49.0, 22.0],
                "id": "obj-584",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "rdiv",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [780.0, 710.0, 28.0, 22.0],
                "id": "obj-585",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "receive",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [860.0, 710.0, 47.0, 22.0],
                "id": "obj-586",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "regexp",
                "numoutlets": 5,
                "outlettype": ["", "", "", "", ""],
                "patching_rect": [940.0, 710.0, 45.0, 22.0],
                "id": "obj-587",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "relativepath",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [1020.0, 710.0, 71.0, 22.0],
                "id": "obj-588",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "rminus",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [1100.0, 710.0, 45.0, 22.0],
                "id": "obj-589",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "round",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [1180.0, 710.0, 39.0, 22.0],
                "id": "obj-590",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "route",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [1260.0, 710.0, 36.0, 22.0],
                "id": "obj-591",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "routepass",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [1340.0, 710.0, 61.0, 22.0],
                "id": "obj-592",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "router",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [1420.0, 710.0, 40.0, 22.0],
                "id": "obj-593",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "rpnin",
                "numoutlets": 4,
                "outlettype": ["int", "int", "int", "int"],
                "patching_rect": [1500.0, 710.0, 35.0, 22.0],
                "id": "obj-594",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "rpnout",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [1580.0, 710.0, 43.0, 22.0],
                "id": "obj-595",
                "numinlets": 4,
            }
        },
        {
            "box": {
                "maxclass": "rslider",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [60.0, 735.0, 20.0, 140.0],
                "id": "obj-597",
                "numinlets": 2,
                "parameter_enable": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "rtin",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [140.0, 735.0, 25.0, 22.0],
                "id": "obj-598",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "savebang",
                "numoutlets": 1,
                "outlettype": ["bang"],
                "patching_rect": [220.0, 735.0, 61.0, 22.0],
                "id": "obj-599",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "savedialog",
                "numoutlets": 3,
                "outlettype": ["", "", "bang"],
                "patching_rect": [300.0, 735.0, 66.0, 22.0],
                "id": "obj-600",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "scale",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [380.0, 735.0, 37.0, 22.0],
                "id": "obj-601",
                "numinlets": 6,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "screensize",
                "numoutlets": 2,
                "outlettype": ["list", "list"],
                "patching_rect": [460.0, 735.0, 66.0, 22.0],
                "id": "obj-602",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "select",
                "numoutlets": 2,
                "outlettype": ["bang", ""],
                "patching_rect": [540.0, 735.0, 40.0, 22.0],
                "id": "obj-603",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "seq",
                "numoutlets": 3,
                "outlettype": ["int", "bang", ""],
                "patching_rect": [620.0, 735.0, 28.0, 22.0],
                "id": "obj-604",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "serial",
                "numoutlets": 2,
                "outlettype": ["int", ""],
                "patching_rect": [700.0, 735.0, 37.0, 22.0],
                "id": "obj-605",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "setclock",
                "numoutlets": 0,
                "patching_rect": [780.0, 735.0, 52.0, 22.0],
                "id": "obj-606",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "shiftleft",
                "numoutlets": 0,
                "patching_rect": [860.0, 735.0, 47.0, 22.0],
                "id": "obj-607",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "shiftright",
                "numoutlets": 0,
                "patching_rect": [940.0, 735.0, 54.0, 22.0],
                "id": "obj-608",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "sin",
                "numoutlets": 1,
                "outlettype": ["float"],
                "patching_rect": [1020.0, 735.0, 24.0, 22.0],
                "id": "obj-609",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "sinh",
                "numoutlets": 1,
                "outlettype": ["float"],
                "patching_rect": [1100.0, 735.0, 31.0, 22.0],
                "id": "obj-610",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "slide",
                "numoutlets": 1,
                "outlettype": ["float"],
                "patching_rect": [1180.0, 735.0, 33.0, 22.0],
                "id": "obj-611",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "slider",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [1260.0, 735.0, 20.0, 140.0],
                "id": "obj-613",
                "numinlets": 1,
                "parameter_enable": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "speedlim",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [1340.0, 735.0, 57.0, 22.0],
                "id": "obj-614",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "spell",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [1420.0, 735.0, 33.0, 22.0],
                "id": "obj-615",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "split",
                "numoutlets": 2,
                "outlettype": ["int", "int"],
                "patching_rect": [1500.0, 735.0, 30.0, 22.0],
                "id": "obj-616",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "spray",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [1580.0, 735.0, 38.0, 22.0],
                "id": "obj-617",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "sprintf",
                "numoutlets": 0,
                "patching_rect": [60.0, 760.0, 41.0, 22.0],
                "id": "obj-618",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "sqrt",
                "numoutlets": 1,
                "outlettype": ["float"],
                "patching_rect": [140.0, 760.0, 29.0, 22.0],
                "id": "obj-619",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "standalone",
                "numoutlets": 0,
                "patching_rect": [220.0, 760.0, 67.0, 22.0],
                "id": "obj-620",
                "numinlets": 1,
                "saved_object_attributes": {
                    "allwindowsactive": 0,
                    "appicon_mac": "",
                    "appicon_win": "",
                    "audiosupport": 1,
                    "bundleidentifier": "com.mycompany.myprogram",
                    "cantclosetoplevelpatchers": 1,
                    "cefsupport": 1,
                    "copysupport": 1,
                    "database": 0,
                    "extensions": 1,
                    "gensupport": 1,
                    "midisupport": 1,
                    "noloadbangdefeating": 0,
                    "overdrive": 0,
                    "preffilename": "",
                    "searchformissingfiles": 1,
                    "statusvisible": 1,
                    "usesearchpath": 0,
                },
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "string.bytes",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [300.0, 760.0, 70.0, 22.0],
                "id": "obj-621",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "string.compare",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [380.0, 760.0, 88.0, 22.0],
                "id": "obj-622",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "string.concat",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [460.0, 760.0, 77.0, 22.0],
                "id": "obj-623",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "string.contains",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [540.0, 760.0, 86.0, 22.0],
                "id": "obj-624",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "string.endswith",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [620.0, 760.0, 89.0, 22.0],
                "id": "obj-625",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "string.frombytes",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [700.0, 760.0, 94.0, 22.0],
                "id": "obj-626",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "string.fromsymlist",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [780.0, 760.0, 102.0, 22.0],
                "id": "obj-627",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "string.fromutf8",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [860.0, 760.0, 85.0, 22.0],
                "id": "obj-628",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "string.index",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [940.0, 760.0, 70.0, 22.0],
                "id": "obj-629",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "string.indexof",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [1020.0, 760.0, 80.0, 22.0],
                "id": "obj-630",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "string.iter",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [1100.0, 760.0, 58.0, 22.0],
                "id": "obj-631",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "string.length",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [1180.0, 760.0, 74.0, 22.0],
                "id": "obj-632",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "string",
                "numoutlets": 3,
                "outlettype": ["", "", ""],
                "patching_rect": [1260.0, 760.0, 38.0, 22.0],
                "id": "obj-633",
                "numinlets": 2,
                "saved_object_attributes": {
                    "parameter_enable": 0,
                    "parameter_mappable": 0,
                },
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "string.remove",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [1340.0, 760.0, 81.0, 22.0],
                "id": "obj-634",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "string.replace",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [1420.0, 760.0, 81.0, 22.0],
                "id": "obj-635",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "string.replaceall",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [1500.0, 760.0, 93.0, 22.0],
                "id": "obj-636",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "string.reverse",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [1580.0, 760.0, 81.0, 22.0],
                "id": "obj-637",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "string.rotate",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [60.0, 785.0, 72.0, 22.0],
                "id": "obj-638",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "string.slice",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [140.0, 785.0, 65.0, 22.0],
                "id": "obj-639",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "string.split",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [220.0, 785.0, 63.0, 22.0],
                "id": "obj-640",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "string.startswith",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [300.0, 785.0, 92.0, 22.0],
                "id": "obj-641",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "string.substring",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [380.0, 785.0, 90.0, 22.0],
                "id": "obj-642",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "string.toarray",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [460.0, 785.0, 79.0, 22.0],
                "id": "obj-643",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "string.tolist",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [540.0, 785.0, 66.0, 22.0],
                "id": "obj-644",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "string.tolower",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [620.0, 785.0, 80.0, 22.0],
                "id": "obj-645",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "string.tosymbol",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [700.0, 785.0, 89.0, 22.0],
                "id": "obj-646",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "string.toupper",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [780.0, 785.0, 82.0, 22.0],
                "id": "obj-647",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "string.trim",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [860.0, 785.0, 61.0, 22.0],
                "id": "obj-648",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "string.trimend",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [940.0, 785.0, 81.0, 22.0],
                "id": "obj-649",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "string.trimstart",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [1020.0, 785.0, 85.0, 22.0],
                "id": "obj-650",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "string.utf8",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [1100.0, 785.0, 61.0, 22.0],
                "id": "obj-651",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "stripnote",
                "numoutlets": 2,
                "outlettype": ["int", "int"],
                "patching_rect": [1180.0, 785.0, 55.0, 22.0],
                "id": "obj-652",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "strippath",
                "numoutlets": 2,
                "outlettype": ["", "int"],
                "patching_rect": [1260.0, 785.0, 55.0, 22.0],
                "id": "obj-653",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "substitute",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [1340.0, 785.0, 60.0, 22.0],
                "id": "obj-654",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "suckah",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [1420.0, 785.0, 100.0, 100.0],
                "id": "obj-656",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "suspend",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [1500.0, 785.0, 54.0, 22.0],
                "id": "obj-657",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "sustain",
                "numoutlets": 2,
                "outlettype": ["int", "int"],
                "patching_rect": [1580.0, 785.0, 47.0, 22.0],
                "id": "obj-658",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "swap",
                "numoutlets": 2,
                "outlettype": ["int", "int"],
                "patching_rect": [60.0, 810.0, 37.0, 22.0],
                "id": "obj-659",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "swatch",
                "numoutlets": 2,
                "outlettype": ["", "float"],
                "patching_rect": [140.0, 810.0, 128.0, 32.0],
                "saturation": 1.0,
                "id": "obj-661",
                "numinlets": 3,
                "parameter_enable": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "switch",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [220.0, 810.0, 42.0, 22.0],
                "id": "obj-662",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "sxformat",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [300.0, 810.0, 55.0, 22.0],
                "id": "obj-663",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "sysexin",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [380.0, 810.0, 49.0, 22.0],
                "id": "obj-664",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "tab",
                "numoutlets": 3,
                "outlettype": ["int", "", ""],
                "patching_rect": [460.0, 810.0, 200.0, 24.0],
                "id": "obj-666",
                "numinlets": 1,
                "parameter_enable": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "table",
                "numoutlets": 2,
                "outlettype": ["int", "bang"],
                "patching_rect": [540.0, 810.0, 35.0, 22.0],
                "id": "obj-667",
                "numinlets": 2,
                "showeditor": 0,
                "embed": 0,
                "editor_rect": [100.0, 100.0, 300.0, 300.0],
                "saved_object_attributes": {
                    "embed": 0,
                    "name": "",
                    "parameter_enable": 0,
                    "parameter_mappable": 0,
                    "range": 128,
                    "showeditor": 0,
                    "size": 128,
                },
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "tan",
                "numoutlets": 1,
                "outlettype": ["float"],
                "patching_rect": [620.0, 810.0, 25.0, 22.0],
                "id": "obj-668",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "tanh",
                "numoutlets": 1,
                "outlettype": ["float"],
                "patching_rect": [700.0, 810.0, 32.0, 22.0],
                "id": "obj-669",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "tempo",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [780.0, 810.0, 42.0, 22.0],
                "id": "obj-670",
                "numinlets": 4,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "text",
                "numoutlets": 3,
                "outlettype": ["", "bang", "int"],
                "patching_rect": [860.0, 810.0, 28.0, 22.0],
                "id": "obj-671",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "textbutton",
                "numoutlets": 3,
                "outlettype": ["", "", "int"],
                "patching_rect": [940.0, 810.0, 100.0, 20.0],
                "id": "obj-673",
                "numinlets": 1,
                "parameter_enable": 0,
            }
        },
        {
            "box": {
                "maxclass": "textedit",
                "numoutlets": 4,
                "outlettype": ["", "int", "", ""],
                "patching_rect": [1020.0, 810.0, 100.0, 50.0],
                "id": "obj-675",
                "numinlets": 1,
                "parameter_enable": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "themecolor",
                "numoutlets": 2,
                "outlettype": ["list", "bang"],
                "patching_rect": [1100.0, 810.0, 68.0, 22.0],
                "id": "obj-676",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "thispatcher",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [1180.0, 810.0, 67.0, 22.0],
                "id": "obj-677",
                "numinlets": 1,
                "save": ["#N", "thispatcher", ";", "#Q", "end", ";"],
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "thresh",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [1260.0, 810.0, 42.0, 22.0],
                "id": "obj-678",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "timepoint",
                "numoutlets": 1,
                "outlettype": ["bang"],
                "patching_rect": [1340.0, 810.0, 57.0, 22.0],
                "id": "obj-679",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "timer",
                "numoutlets": 2,
                "outlettype": ["float", ""],
                "patching_rect": [1420.0, 810.0, 35.0, 22.0],
                "id": "obj-680",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "times",
                "numoutlets": 0,
                "patching_rect": [1500.0, 810.0, 37.0, 22.0],
                "id": "obj-681",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "togedge",
                "numoutlets": 2,
                "outlettype": ["bang", "bang"],
                "patching_rect": [1580.0, 810.0, 52.0, 22.0],
                "id": "obj-682",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "toggle",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [60.0, 835.0, 24.0, 24.0],
                "id": "obj-684",
                "numinlets": 1,
                "parameter_enable": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "tosymbol",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [140.0, 835.0, 57.0, 22.0],
                "id": "obj-685",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "touchin",
                "numoutlets": 2,
                "outlettype": ["int", "int"],
                "patching_rect": [220.0, 835.0, 47.0, 22.0],
                "id": "obj-686",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "touchout",
                "numoutlets": 0,
                "patching_rect": [300.0, 835.0, 55.0, 22.0],
                "id": "obj-687",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "translate",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [380.0, 835.0, 55.0, 22.0],
                "id": "obj-688",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "transport",
                "numoutlets": 9,
                "outlettype": [
                    "int",
                    "int",
                    "float",
                    "float",
                    "float",
                    "",
                    "int",
                    "float",
                    "",
                ],
                "patching_rect": [460.0, 835.0, 56.0, 22.0],
                "id": "obj-689",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "trigger",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [540.0, 835.0, 43.0, 22.0],
                "id": "obj-690",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "trough",
                "numoutlets": 3,
                "outlettype": ["int", "int", "int"],
                "patching_rect": [620.0, 835.0, 43.0, 22.0],
                "id": "obj-691",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "ubutton",
                "numoutlets": 4,
                "handoff": "",
                "outlettype": ["bang", "bang", "", "int"],
                "patching_rect": [700.0, 835.0, 33.0, 42.0],
                "id": "obj-693",
                "numinlets": 1,
                "parameter_enable": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "udpreceive",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [780.0, 835.0, 67.0, 22.0],
                "id": "obj-694",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "udpsend",
                "numoutlets": 0,
                "patching_rect": [860.0, 835.0, 55.0, 22.0],
                "id": "obj-695",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "umenu",
                "numoutlets": 3,
                "items": "<empty>",
                "outlettype": ["int", "", ""],
                "patching_rect": [940.0, 835.0, 100.0, 22.0],
                "id": "obj-697",
                "numinlets": 1,
                "parameter_enable": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "universal",
                "numoutlets": 0,
                "patching_rect": [1020.0, 835.0, 57.0, 22.0],
                "id": "obj-698",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "unjoin",
                "numoutlets": 3,
                "outlettype": ["", "", ""],
                "patching_rect": [1100.0, 835.0, 41.0, 22.0],
                "id": "obj-699",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "unpack",
                "numoutlets": 2,
                "outlettype": ["int", "int"],
                "patching_rect": [1180.0, 835.0, 47.0, 22.0],
                "id": "obj-700",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "urn",
                "numoutlets": 2,
                "outlettype": ["int", "bang"],
                "patching_rect": [1260.0, 835.0, 26.0, 22.0],
                "id": "obj-701",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "uzi",
                "numoutlets": 3,
                "outlettype": ["bang", "bang", "int"],
                "patching_rect": [1340.0, 835.0, 24.0, 22.0],
                "id": "obj-702",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "value",
                "numoutlets": 0,
                "patching_rect": [1420.0, 835.0, 37.0, 22.0],
                "id": "obj-703",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "vdp",
                "numoutlets": 4,
                "outlettype": ["", "bang", "int", ""],
                "patching_rect": [1500.0, 835.0, 28.0, 22.0],
                "id": "obj-704",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "vexpr",
                "numoutlets": 0,
                "patching_rect": [1580.0, 835.0, 38.0, 22.0],
                "id": "obj-705",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "vstscan",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [60.0, 860.0, 49.0, 22.0],
                "id": "obj-706",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "when",
                "numoutlets": 2,
                "outlettype": ["list", "float"],
                "patching_rect": [140.0, 860.0, 37.0, 22.0],
                "id": "obj-707",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "xbendin",
                "numoutlets": 2,
                "outlettype": ["int", "int"],
                "patching_rect": [220.0, 860.0, 51.0, 22.0],
                "id": "obj-708",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "xbendout",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [300.0, 860.0, 58.0, 22.0],
                "id": "obj-709",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "xctlin",
                "numoutlets": 3,
                "outlettype": ["int", "int", "int"],
                "patching_rect": [380.0, 860.0, 36.0, 22.0],
                "id": "obj-710",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "xctlout",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [460.0, 860.0, 43.0, 22.0],
                "id": "obj-711",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "xmidiin",
                "numoutlets": 2,
                "outlettype": ["int", ""],
                "patching_rect": [540.0, 860.0, 46.0, 22.0],
                "id": "obj-712",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "xnotein",
                "numoutlets": 4,
                "outlettype": ["int", "int", "int", "int"],
                "patching_rect": [620.0, 860.0, 47.0, 22.0],
                "id": "obj-713",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "xnoteout",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [700.0, 860.0, 55.0, 22.0],
                "id": "obj-714",
                "numinlets": 4,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "zl.change",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [780.0, 860.0, 60.0, 22.0],
                "id": "obj-715",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "zl.compare",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [860.0, 860.0, 67.0, 22.0],
                "id": "obj-716",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "zl.delace",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [940.0, 860.0, 56.0, 22.0],
                "id": "obj-717",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "zl.ecils",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [1020.0, 860.0, 45.0, 22.0],
                "id": "obj-718",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "zl.filter",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [1100.0, 860.0, 43.0, 22.0],
                "id": "obj-719",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "zl.group",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [1180.0, 860.0, 51.0, 22.0],
                "id": "obj-720",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "zl.indexmap",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [1260.0, 860.0, 73.0, 22.0],
                "id": "obj-721",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "zl.iter",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [1340.0, 860.0, 37.0, 22.0],
                "id": "obj-722",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "zl.join",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [1420.0, 860.0, 39.0, 22.0],
                "id": "obj-723",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "zl.lace",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [1500.0, 860.0, 43.0, 22.0],
                "id": "obj-724",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "zl.len",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [1580.0, 860.0, 37.0, 22.0],
                "id": "obj-725",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "zl.lookup",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [60.0, 885.0, 56.0, 22.0],
                "id": "obj-726",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "zl",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [140.0, 885.0, 18.0, 22.0],
                "id": "obj-727",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "zl.median",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [220.0, 885.0, 60.0, 22.0],
                "id": "obj-728",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "zl.mth",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [300.0, 885.0, 41.0, 22.0],
                "id": "obj-729",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "zl.nth",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [380.0, 885.0, 37.0, 22.0],
                "id": "obj-730",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "zl.queue",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [460.0, 885.0, 54.0, 22.0],
                "id": "obj-731",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "zl.reg",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [540.0, 885.0, 38.0, 22.0],
                "id": "obj-732",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "zl.rev",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [620.0, 885.0, 37.0, 22.0],
                "id": "obj-733",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "zl.rot",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [700.0, 885.0, 35.0, 22.0],
                "id": "obj-734",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "zl.scramble",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [780.0, 885.0, 69.0, 22.0],
                "id": "obj-735",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "zl.sect",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [860.0, 885.0, 43.0, 22.0],
                "id": "obj-736",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "zl.slice",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [940.0, 885.0, 45.0, 22.0],
                "id": "obj-737",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "zl.sort",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [1020.0, 885.0, 41.0, 22.0],
                "id": "obj-738",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "zl.stack",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [1100.0, 885.0, 49.0, 22.0],
                "id": "obj-739",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "zl.stream",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [1180.0, 885.0, 57.0, 22.0],
                "id": "obj-740",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "zl.sub",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [1260.0, 885.0, 40.0, 22.0],
                "id": "obj-741",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "zl.sum",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [1340.0, 885.0, 43.0, 22.0],
                "id": "obj-742",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "zl.swap",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [1420.0, 885.0, 49.0, 22.0],
                "id": "obj-743",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "zl.thin",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [1500.0, 885.0, 40.0, 22.0],
                "id": "obj-744",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "zl.union",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [1580.0, 885.0, 50.0, 22.0],
                "id": "obj-745",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "zl.unique",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [60.0, 910.0, 57.0, 22.0],
                "id": "obj-746",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "zmap",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [140.0, 910.0, 38.0, 22.0],
                "id": "obj-747",
                "numinlets": 5,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "2d.wave~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [220.0, 910.0, 60.0, 22.0],
                "id": "obj-748",
                "numinlets": 4,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "abs~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [300.0, 910.0, 35.0, 22.0],
                "id": "obj-749",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "acosh~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [380.0, 910.0, 48.0, 22.0],
                "id": "obj-750",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "acos~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [460.0, 910.0, 41.0, 22.0],
                "id": "obj-751",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "adc~",
                "numoutlets": 2,
                "outlettype": ["signal", "signal"],
                "patching_rect": [540.0, 910.0, 35.0, 22.0],
                "id": "obj-752",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "adoutput~",
                "numoutlets": 2,
                "outlettype": ["signal", "signal"],
                "patching_rect": [620.0, 910.0, 62.0, 22.0],
                "id": "obj-753",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "adsr~",
                "numoutlets": 4,
                "outlettype": ["signal", "signal", "", ""],
                "patching_rect": [700.0, 910.0, 39.0, 22.0],
                "id": "obj-754",
                "numinlets": 5,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "adstatus",
                "numoutlets": 0,
                "patching_rect": [780.0, 910.0, 54.0, 22.0],
                "id": "obj-755",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "allpass~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [860.0, 910.0, 53.0, 22.0],
                "id": "obj-756",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "varname": "amxd~",
                "viewvisibility": 0,
                "offset": [0.0, 0.0],
                "lockeddragscroll": 0,
                "clickthrough": 0,
                "enablehscroll": 0,
                "enablevscroll": 0,
                "lockedsize": 0,
                "bgmode": 1,
                "border": 0,
                "text": "amxd~",
                "numoutlets": 4,
                "outlettype": ["signal", "signal", "", ""],
                "patching_rect": [940.0, 910.0, 45.0, 22.0],
                "id": "obj-757",
                "numinlets": 3,
                "autosave": 1,
                "saved_object_attributes": {
                    "parameter_enable": 1,
                    "patchername": "",
                    "patchername_fallback": "/Volumes/<none>/",
                },
                "saved_attribute_attributes": {
                    "valueof": {
                        "parameter_invisible": 1,
                        "parameter_longname": "amxd~",
                        "parameter_shortname": "amxd~",
                        "parameter_type": 3,
                    }
                },
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "asinh~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1020.0, 910.0, 44.0, 22.0],
                "id": "obj-758",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "asin~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1100.0, 910.0, 38.0, 22.0],
                "id": "obj-759",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "atan2~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1180.0, 910.0, 46.0, 22.0],
                "id": "obj-760",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "atanh~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1260.0, 910.0, 46.0, 22.0],
                "id": "obj-761",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "atan~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1340.0, 910.0, 39.0, 22.0],
                "id": "obj-762",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "atodb~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1420.0, 910.0, 46.0, 22.0],
                "id": "obj-763",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "average~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1500.0, 910.0, 59.0, 22.0],
                "id": "obj-764",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "avg~",
                "numoutlets": 1,
                "outlettype": ["float"],
                "patching_rect": [1580.0, 910.0, 35.0, 22.0],
                "id": "obj-765",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "begin~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [60.0, 935.0, 45.0, 22.0],
                "id": "obj-766",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "biquad~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [140.0, 935.0, 52.0, 22.0],
                "id": "obj-767",
                "numinlets": 6,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "bitand~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [220.0, 935.0, 48.0, 22.0],
                "id": "obj-768",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "bitnot~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [300.0, 935.0, 45.0, 22.0],
                "id": "obj-769",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "bitor~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [380.0, 935.0, 39.0, 22.0],
                "id": "obj-770",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "bitsafe~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [460.0, 935.0, 51.0, 22.0],
                "id": "obj-771",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "bitshift~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [540.0, 935.0, 50.0, 22.0],
                "id": "obj-772",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "bitxor~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [620.0, 935.0, 45.0, 22.0],
                "id": "obj-773",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "buffer~",
                "numoutlets": 2,
                "outlettype": ["float", "bang"],
                "patching_rect": [700.0, 935.0, 46.0, 22.0],
                "id": "obj-774",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "buffir~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [780.0, 935.0, 42.0, 22.0],
                "id": "obj-775",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "capture~",
                "numoutlets": 0,
                "patching_rect": [860.0, 935.0, 56.0, 22.0],
                "id": "obj-776",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "cartopol~",
                "numoutlets": 2,
                "outlettype": ["signal", "signal"],
                "patching_rect": [940.0, 935.0, 58.0, 22.0],
                "id": "obj-777",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "cascade~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1020.0, 935.0, 60.0, 22.0],
                "id": "obj-778",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "change~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1100.0, 935.0, 55.0, 22.0],
                "id": "obj-779",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "click~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1180.0, 935.0, 39.0, 22.0],
                "id": "obj-780",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "clip~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1260.0, 935.0, 34.0, 22.0],
                "id": "obj-781",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "comb~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1340.0, 935.0, 45.0, 22.0],
                "id": "obj-782",
                "numinlets": 5,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "cosh~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1420.0, 935.0, 41.0, 22.0],
                "id": "obj-783",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "cosx~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1500.0, 935.0, 40.0, 22.0],
                "id": "obj-784",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "cos~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1580.0, 935.0, 34.0, 22.0],
                "id": "obj-785",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "count~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [60.0, 960.0, 45.0, 22.0],
                "id": "obj-786",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "cross~",
                "numoutlets": 2,
                "outlettype": ["signal", "signal"],
                "patching_rect": [140.0, 960.0, 44.0, 22.0],
                "id": "obj-787",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "curve~",
                "numoutlets": 2,
                "outlettype": ["signal", "bang"],
                "patching_rect": [220.0, 960.0, 45.0, 22.0],
                "id": "obj-788",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "cycle~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [300.0, 960.0, 43.0, 22.0],
                "id": "obj-789",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "dac~",
                "numoutlets": 0,
                "patching_rect": [380.0, 960.0, 35.0, 22.0],
                "id": "obj-790",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "dbtoa~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [460.0, 960.0, 46.0, 22.0],
                "id": "obj-791",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "degrade~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [540.0, 960.0, 60.0, 22.0],
                "id": "obj-792",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "delay~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [620.0, 960.0, 44.0, 22.0],
                "id": "obj-793",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "deltaclip~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [700.0, 960.0, 60.0, 22.0],
                "id": "obj-794",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "delta~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [780.0, 960.0, 42.0, 22.0],
                "id": "obj-795",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "div~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [860.0, 960.0, 31.0, 22.0],
                "id": "obj-796",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "downsamp~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [940.0, 960.0, 74.0, 22.0],
                "id": "obj-797",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "dspstate~",
                "numoutlets": 4,
                "outlettype": ["int", "float", "int", "int"],
                "patching_rect": [1020.0, 960.0, 61.0, 22.0],
                "id": "obj-798",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "dsptime~",
                "numoutlets": 1,
                "outlettype": ["float"],
                "patching_rect": [1100.0, 960.0, 58.0, 22.0],
                "id": "obj-799",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "edge~",
                "numoutlets": 2,
                "outlettype": ["bang", "bang"],
                "patching_rect": [1180.0, 960.0, 42.0, 22.0],
                "id": "obj-800",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "equals~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1260.0, 960.0, 51.0, 22.0],
                "id": "obj-801",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "ezadc~",
                "numoutlets": 2,
                "outlettype": ["signal", "signal"],
                "patching_rect": [1340.0, 960.0, 45.0, 45.0],
                "id": "obj-803",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "ezdac~",
                "numoutlets": 0,
                "patching_rect": [1420.0, 960.0, 45.0, 45.0],
                "id": "obj-805",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "fbinshift~",
                "numoutlets": 2,
                "outlettype": ["signal", "signal"],
                "patching_rect": [1500.0, 960.0, 57.0, 22.0],
                "id": "obj-806",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "fffb~",
                "numoutlets": 4,
                "outlettype": ["signal", "signal", "signal", "signal"],
                "patching_rect": [1580.0, 960.0, 32.0, 22.0],
                "id": "obj-807",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "fftinfo~",
                "numoutlets": 4,
                "outlettype": ["int", "int", "int", "int"],
                "patching_rect": [60.0, 985.0, 45.0, 22.0],
                "id": "obj-808",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "fftin~",
                "numoutlets": 0,
                "patching_rect": [140.0, 985.0, 35.0, 22.0],
                "id": "obj-809",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "fftout~",
                "numoutlets": 0,
                "patching_rect": [220.0, 985.0, 42.0, 22.0],
                "id": "obj-810",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "fft~",
                "numoutlets": 3,
                "outlettype": ["signal", "signal", "signal"],
                "patching_rect": [300.0, 985.0, 25.0, 22.0],
                "id": "obj-811",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "filtercoeff~",
                "numoutlets": 5,
                "outlettype": ["signal", "signal", "signal", "signal", "signal"],
                "patching_rect": [380.0, 985.0, 64.0, 22.0],
                "id": "obj-812",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "filterdesign",
                "numoutlets": 1,
                "outlettype": ["dictionary"],
                "patching_rect": [460.0, 985.0, 67.0, 22.0],
                "id": "obj-813",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "filterdetail",
                "numoutlets": 6,
                "outlettype": ["", "", "", "", "", ""],
                "patching_rect": [540.0, 985.0, 60.0, 22.0],
                "id": "obj-814",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "filtergraph~",
                "numoutlets": 7,
                "fontface": 0,
                "outlettype": [
                    "list",
                    "float",
                    "float",
                    "float",
                    "float",
                    "list",
                    "int",
                ],
                "patching_rect": [620.0, 985.0, 256.0, 128.0],
                "id": "obj-816",
                "numinlets": 8,
                "parameter_enable": 0,
                "nfilters": 1,
                "setfilter": [
                    0,
                    5,
                    1,
                    0,
                    0,
                    40.0,
                    1.0,
                    2.5,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                ],
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "frameaccum~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [700.0, 985.0, 82.0, 22.0],
                "id": "obj-817",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "frameaverage~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [780.0, 985.0, 90.0, 22.0],
                "id": "obj-818",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "framedelta~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [860.0, 985.0, 72.0, 22.0],
                "id": "obj-819",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "framesmooth~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [940.0, 985.0, 86.0, 22.0],
                "id": "obj-820",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "framesnap~",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [1020.0, 985.0, 72.0, 22.0],
                "id": "obj-821",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "frame~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1100.0, 985.0, 46.0, 22.0],
                "id": "obj-822",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "freqshift~",
                "numoutlets": 2,
                "outlettype": ["signal", "signal"],
                "patching_rect": [1180.0, 985.0, 58.0, 22.0],
                "id": "obj-823",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "ftom~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1260.0, 985.0, 39.0, 22.0],
                "id": "obj-824",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "fzero~",
                "numoutlets": 3,
                "outlettype": ["float", "float", ""],
                "patching_rect": [1340.0, 985.0, 42.0, 22.0],
                "id": "obj-825",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "gain~",
                "numoutlets": 2,
                "multichannelvariant": 0,
                "outlettype": ["signal", ""],
                "patching_rect": [1420.0, 985.0, 22.0, 140.0],
                "id": "obj-827",
                "numinlets": 1,
                "parameter_enable": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "gate~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1500.0, 985.0, 39.0, 22.0],
                "id": "obj-828",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "gen",
                "numoutlets": 1,
                "outlettype": ["float"],
                "patching_rect": [1580.0, 985.0, 29.0, 22.0],
                "id": "obj-829",
                "numinlets": 2,
                "patcher": {
                    "fileversion": 1,
                    "appversion": {
                        "major": 8,
                        "minor": 6,
                        "revision": 0,
                        "architecture": "x64",
                        "modernui": 1,
                    },
                    "classnamespace": "dsp.gen",
                    "rect": [0.0, 0.0, 600.0, 450.0],
                    "bglocked": 0,
                    "openinpresentation": 0,
                    "default_fontsize": 12.0,
                    "default_fontface": 0,
                    "default_fontname": "Arial",
                    "gridonopen": 1,
                    "gridsize": [15.0, 15.0],
                    "gridsnaponopen": 1,
                    "objectsnaponopen": 1,
                    "statusbarvisible": 2,
                    "toolbarvisible": 1,
                    "lefttoolbarpinned": 0,
                    "toptoolbarpinned": 0,
                    "righttoolbarpinned": 0,
                    "bottomtoolbarpinned": 0,
                    "toolbars_unpinned_last_save": 0,
                    "tallnewobj": 0,
                    "boxanimatetime": 200,
                    "enablehscroll": 1,
                    "enablevscroll": 1,
                    "devicewidth": 0.0,
                    "description": "",
                    "digest": "",
                    "tags": "",
                    "style": "",
                    "subpatcher_template": "",
                    "assistshowspatchername": 0,
                    "boxes": [
                        {
                            "box": {
                                "maxclass": "newobj",
                                "text": "in 1",
                                "numoutlets": 1,
                                "outlettype": [""],
                                "patching_rect": [50.0, 14.0, 28.0, 22.0],
                                "id": "obj-1",
                                "numinlets": 0,
                            }
                        },
                        {
                            "box": {
                                "maxclass": "newobj",
                                "text": "in 2",
                                "numoutlets": 1,
                                "outlettype": [""],
                                "patching_rect": [305.0, 14.0, 28.0, 22.0],
                                "id": "obj-2",
                                "numinlets": 0,
                            }
                        },
                        {
                            "box": {
                                "maxclass": "newobj",
                                "text": "+",
                                "numoutlets": 1,
                                "outlettype": [""],
                                "patching_rect": [176.0, 149.0, 29.5, 22.0],
                                "id": "obj-3",
                                "numinlets": 2,
                            }
                        },
                        {
                            "box": {
                                "maxclass": "newobj",
                                "text": "out 1",
                                "numoutlets": 0,
                                "patching_rect": [176.0, 418.0, 35.0, 22.0],
                                "id": "obj-4",
                                "numinlets": 1,
                            }
                        },
                    ],
                    "lines": [
                        {
                            "patchline": {
                                "source": ["obj-3", 0],
                                "destination": ["obj-4", 0],
                            }
                        },
                        {
                            "patchline": {
                                "source": ["obj-2", 0],
                                "destination": ["obj-3", 1],
                            }
                        },
                        {
                            "patchline": {
                                "source": ["obj-1", 0],
                                "destination": ["obj-3", 0],
                            }
                        },
                    ],
                },
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "gen~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [60.0, 1010.0, 36.0, 22.0],
                "id": "obj-830",
                "numinlets": 2,
                "patcher": {
                    "fileversion": 1,
                    "appversion": {
                        "major": 8,
                        "minor": 6,
                        "revision": 0,
                        "architecture": "x64",
                        "modernui": 1,
                    },
                    "classnamespace": "dsp.gen",
                    "rect": [0.0, 0.0, 600.0, 450.0],
                    "bglocked": 0,
                    "openinpresentation": 0,
                    "default_fontsize": 12.0,
                    "default_fontface": 0,
                    "default_fontname": "Arial",
                    "gridonopen": 1,
                    "gridsize": [15.0, 15.0],
                    "gridsnaponopen": 1,
                    "objectsnaponopen": 1,
                    "statusbarvisible": 2,
                    "toolbarvisible": 1,
                    "lefttoolbarpinned": 0,
                    "toptoolbarpinned": 0,
                    "righttoolbarpinned": 0,
                    "bottomtoolbarpinned": 0,
                    "toolbars_unpinned_last_save": 0,
                    "tallnewobj": 0,
                    "boxanimatetime": 200,
                    "enablehscroll": 1,
                    "enablevscroll": 1,
                    "devicewidth": 0.0,
                    "description": "",
                    "digest": "",
                    "tags": "",
                    "style": "",
                    "subpatcher_template": "",
                    "assistshowspatchername": 0,
                    "boxes": [
                        {
                            "box": {
                                "maxclass": "newobj",
                                "text": "in 1",
                                "numoutlets": 1,
                                "outlettype": [""],
                                "patching_rect": [50.0, 14.0, 28.0, 22.0],
                                "id": "obj-1",
                                "numinlets": 0,
                            }
                        },
                        {
                            "box": {
                                "maxclass": "newobj",
                                "text": "in 2",
                                "numoutlets": 1,
                                "outlettype": [""],
                                "patching_rect": [305.0, 14.0, 28.0, 22.0],
                                "id": "obj-2",
                                "numinlets": 0,
                            }
                        },
                        {
                            "box": {
                                "maxclass": "newobj",
                                "text": "+",
                                "numoutlets": 1,
                                "outlettype": [""],
                                "patching_rect": [176.0, 149.0, 29.5, 22.0],
                                "id": "obj-3",
                                "numinlets": 2,
                            }
                        },
                        {
                            "box": {
                                "maxclass": "newobj",
                                "text": "out 1",
                                "numoutlets": 0,
                                "patching_rect": [176.0, 418.0, 35.0, 22.0],
                                "id": "obj-4",
                                "numinlets": 1,
                            }
                        },
                    ],
                    "lines": [
                        {
                            "patchline": {
                                "source": ["obj-3", 0],
                                "destination": ["obj-4", 0],
                            }
                        },
                        {
                            "patchline": {
                                "source": ["obj-2", 0],
                                "destination": ["obj-3", 1],
                            }
                        },
                        {
                            "patchline": {
                                "source": ["obj-1", 0],
                                "destination": ["obj-3", 0],
                            }
                        },
                    ],
                },
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "gizmo~",
                "numoutlets": 2,
                "outlettype": ["signal", "signal"],
                "patching_rect": [140.0, 1010.0, 48.0, 22.0],
                "id": "obj-831",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "greaterthaneq~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [220.0, 1010.0, 90.0, 22.0],
                "id": "obj-832",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "greaterthan~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [300.0, 1010.0, 77.0, 22.0],
                "id": "obj-833",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "gridmeter~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [380.0, 1010.0, 20.0, 16.0],
                "id": "obj-835",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "groove~",
                "numoutlets": 2,
                "outlettype": ["signal", "signal"],
                "patching_rect": [460.0, 1010.0, 52.0, 22.0],
                "id": "obj-836",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "hilbert~",
                "numoutlets": 2,
                "outlettype": ["signal", "signal"],
                "patching_rect": [540.0, 1010.0, 48.0, 22.0],
                "id": "obj-837",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "hostcontrol~",
                "numoutlets": 0,
                "patching_rect": [620.0, 1010.0, 74.0, 22.0],
                "id": "obj-838",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "hostphasor~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [700.0, 1010.0, 75.0, 22.0],
                "id": "obj-839",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "hostsync~",
                "numoutlets": 10,
                "outlettype": [
                    "int",
                    "int",
                    "int",
                    "float",
                    "list",
                    "float",
                    "float",
                    "int",
                    "list",
                    "int",
                ],
                "patching_rect": [780.0, 1010.0, 63.0, 22.0],
                "id": "obj-840",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "ifft~",
                "numoutlets": 3,
                "outlettype": ["signal", "signal", "signal"],
                "patching_rect": [860.0, 1010.0, 28.0, 22.0],
                "id": "obj-841",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "in",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [940.0, 1010.0, 18.0, 22.0],
                "id": "obj-842",
                "numinlets": 1,
                "saved_object_attributes": {"attr_comment": ""},
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "index~",
                "numoutlets": 0,
                "patching_rect": [1020.0, 1010.0, 44.0, 22.0],
                "id": "obj-843",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "info~",
                "numoutlets": 9,
                "outlettype": [
                    "float",
                    "list",
                    "float",
                    "float",
                    "float",
                    "float",
                    "float",
                    "",
                    "int",
                ],
                "patching_rect": [1100.0, 1010.0, 35.0, 22.0],
                "id": "obj-844",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "in~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1180.0, 1010.0, 25.0, 22.0],
                "id": "obj-845",
                "numinlets": 1,
                "saved_object_attributes": {"attr_comment": ""},
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "ioscbank~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1260.0, 1010.0, 63.0, 22.0],
                "id": "obj-846",
                "numinlets": 4,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "kink~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1340.0, 1010.0, 37.0, 22.0],
                "id": "obj-847",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "lessthaneq~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1420.0, 1010.0, 74.0, 22.0],
                "id": "obj-848",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "lessthan~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1500.0, 1010.0, 60.0, 22.0],
                "id": "obj-849",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "levelmeter~",
                "numoutlets": 1,
                "markersused": 8,
                "outlettype": [""],
                "patching_rect": [1580.0, 1010.0, 128.0, 64.0],
                "id": "obj-851",
                "markers": [-60, -48, -36, -24, -12, -6, 0, 6],
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "limi~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [60.0, 1035.0, 34.0, 22.0],
                "id": "obj-852",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "line~",
                "numoutlets": 2,
                "outlettype": ["signal", "bang"],
                "patching_rect": [140.0, 1035.0, 34.0, 22.0],
                "id": "obj-853",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "log~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [220.0, 1035.0, 32.0, 22.0],
                "id": "obj-854",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "lookup~",
                "numoutlets": 0,
                "patching_rect": [300.0, 1035.0, 51.0, 22.0],
                "id": "obj-855",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "lores~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [380.0, 1035.0, 42.0, 22.0],
                "id": "obj-856",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "matrix~",
                "numoutlets": 3,
                "outlettype": ["signal", "signal", ""],
                "patching_rect": [460.0, 1035.0, 48.0, 22.0],
                "id": "obj-857",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "maximum~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [540.0, 1035.0, 68.0, 22.0],
                "id": "obj-858",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.2d.wave~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [620.0, 1035.0, 80.0, 22.0],
                "id": "obj-859",
                "numinlets": 4,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.abs~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [700.0, 1035.0, 54.0, 22.0],
                "id": "obj-860",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.acosh~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [780.0, 1035.0, 67.0, 22.0],
                "id": "obj-861",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.acos~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [860.0, 1035.0, 60.0, 22.0],
                "id": "obj-862",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.adc~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [940.0, 1035.0, 54.0, 22.0],
                "id": "obj-863",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.adsr~",
                "numoutlets": 5,
                "outlettype": ["multichannelsignal", "multichannelsignal", "", "", ""],
                "patching_rect": [1020.0, 1035.0, 58.0, 22.0],
                "id": "obj-864",
                "numinlets": 5,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.allpass~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [1100.0, 1035.0, 72.0, 22.0],
                "id": "obj-865",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "varname": "amxd~[1]",
                "viewvisibility": 0,
                "offset": [0.0, 0.0],
                "lockeddragscroll": 0,
                "clickthrough": 0,
                "enablehscroll": 0,
                "enablevscroll": 0,
                "lockedsize": 0,
                "bgmode": 0,
                "border": 0,
                "text": "mc.amxd~",
                "numoutlets": 5,
                "outlettype": ["multichannelsignal", "multichannelsignal", "", "", ""],
                "patching_rect": [1180.0, 1035.0, 64.0, 22.0],
                "id": "obj-866",
                "numinlets": 3,
                "data": {"autosave": 1},
                "saved_object_attributes": {
                    "parameter_enable": 1,
                    "patchername": "",
                    "patchername_fallback": "/Volumes/<none>/",
                },
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.apply~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [1260.0, 1035.0, 64.0, 22.0],
                "id": "obj-867",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.asinh~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [1340.0, 1035.0, 64.0, 22.0],
                "id": "obj-868",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.asin~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [1420.0, 1035.0, 57.0, 22.0],
                "id": "obj-869",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.assign",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [1500.0, 1035.0, 63.0, 22.0],
                "id": "obj-870",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.atan2~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [1580.0, 1035.0, 65.0, 22.0],
                "id": "obj-871",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.atanh~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [60.0, 1060.0, 65.0, 22.0],
                "id": "obj-872",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.atan~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [140.0, 1060.0, 58.0, 22.0],
                "id": "obj-873",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.atodb~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [220.0, 1060.0, 65.0, 22.0],
                "id": "obj-874",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.average~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [300.0, 1060.0, 78.0, 22.0],
                "id": "obj-875",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.avg~",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [380.0, 1060.0, 54.0, 22.0],
                "id": "obj-876",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.bands~",
                "numoutlets": 3,
                "outlettype": ["multichannelsignal", "", "float"],
                "patching_rect": [460.0, 1060.0, 68.0, 22.0],
                "id": "obj-877",
                "numinlets": 5,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.biquad~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [540.0, 1060.0, 71.0, 22.0],
                "id": "obj-878",
                "numinlets": 6,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.bitand~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [620.0, 1060.0, 68.0, 22.0],
                "id": "obj-879",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.bitnot~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [700.0, 1060.0, 64.0, 22.0],
                "id": "obj-880",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.bitor~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [780.0, 1060.0, 58.0, 22.0],
                "id": "obj-881",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.bitsafe~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [860.0, 1060.0, 70.0, 22.0],
                "id": "obj-882",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.bitxor~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [940.0, 1060.0, 64.0, 22.0],
                "id": "obj-883",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.buffir~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [1020.0, 1060.0, 61.0, 22.0],
                "id": "obj-884",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.cartopol~",
                "numoutlets": 2,
                "outlettype": ["multichannelsignal", "multichannelsignal"],
                "patching_rect": [1100.0, 1060.0, 78.0, 22.0],
                "id": "obj-885",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.cascade~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [1180.0, 1060.0, 80.0, 22.0],
                "id": "obj-886",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.cell",
                "numoutlets": 1,
                "outlettype": ["setvalue"],
                "patching_rect": [1260.0, 1060.0, 46.0, 22.0],
                "id": "obj-887",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.change~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [1340.0, 1060.0, 74.0, 22.0],
                "id": "obj-888",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.channelcount~",
                "numoutlets": 2,
                "outlettype": ["int", "signal"],
                "patching_rect": [1420.0, 1060.0, 106.0, 22.0],
                "id": "obj-889",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.chord~",
                "numoutlets": 4,
                "outlettype": [
                    "multichannelsignal",
                    "multichannelsignal",
                    "list",
                    "int",
                ],
                "patching_rect": [1500.0, 1060.0, 65.0, 22.0],
                "id": "obj-890",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.click~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [1580.0, 1060.0, 58.0, 22.0],
                "id": "obj-891",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.clip~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [60.0, 1085.0, 53.0, 22.0],
                "id": "obj-892",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.combine~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [140.0, 1085.0, 80.0, 22.0],
                "id": "obj-893",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.comb~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [220.0, 1085.0, 64.0, 22.0],
                "id": "obj-894",
                "numinlets": 5,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.cosh~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [300.0, 1085.0, 60.0, 22.0],
                "id": "obj-895",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.cosx~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [380.0, 1085.0, 60.0, 22.0],
                "id": "obj-896",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.cos~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [460.0, 1085.0, 54.0, 22.0],
                "id": "obj-897",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.count~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [540.0, 1085.0, 64.0, 22.0],
                "id": "obj-898",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.cross~",
                "numoutlets": 2,
                "outlettype": ["multichannelsignal", "multichannelsignal"],
                "patching_rect": [620.0, 1085.0, 64.0, 22.0],
                "id": "obj-899",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.curve~",
                "numoutlets": 3,
                "outlettype": ["multichannelsignal", "", ""],
                "patching_rect": [700.0, 1085.0, 64.0, 22.0],
                "id": "obj-900",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.cycle~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [780.0, 1085.0, 62.0, 22.0],
                "id": "obj-901",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.dac~",
                "numoutlets": 0,
                "patching_rect": [860.0, 1085.0, 54.0, 22.0],
                "id": "obj-902",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.dbtoa~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [940.0, 1085.0, 65.0, 22.0],
                "id": "obj-903",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.degrade~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [1020.0, 1085.0, 79.0, 22.0],
                "id": "obj-904",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.deinterleave~",
                "numoutlets": 2,
                "outlettype": ["multichannelsignal", "multichannelsignal"],
                "patching_rect": [1100.0, 1085.0, 100.0, 22.0],
                "id": "obj-905",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.delay~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [1180.0, 1085.0, 64.0, 22.0],
                "id": "obj-906",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.deltaclip~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [1260.0, 1085.0, 79.0, 22.0],
                "id": "obj-907",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.delta~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [1340.0, 1085.0, 61.0, 22.0],
                "id": "obj-908",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.div~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [1420.0, 1085.0, 50.0, 22.0],
                "id": "obj-909",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.downsamp~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [1500.0, 1085.0, 93.0, 22.0],
                "id": "obj-910",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.dup~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [1580.0, 1085.0, 55.0, 22.0],
                "id": "obj-911",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.edge~",
                "numoutlets": 3,
                "outlettype": ["", "", ""],
                "patching_rect": [60.0, 1110.0, 62.0, 22.0],
                "id": "obj-912",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.equals~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [140.0, 1110.0, 70.0, 22.0],
                "id": "obj-913",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.evolve~",
                "numoutlets": 3,
                "outlettype": ["multichannelsignal", "float", "list"],
                "patching_rect": [220.0, 1110.0, 70.0, 22.0],
                "id": "obj-914",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "mc.ezadc~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [300.0, 1110.0, 45.0, 45.0],
                "id": "obj-916",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "mc.ezdac~",
                "numoutlets": 0,
                "patching_rect": [380.0, 1110.0, 45.0, 45.0],
                "id": "obj-918",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.fffb~",
                "numoutlets": 4,
                "outlettype": [
                    "multichannelsignal",
                    "multichannelsignal",
                    "multichannelsignal",
                    "multichannelsignal",
                ],
                "patching_rect": [460.0, 1110.0, 51.0, 22.0],
                "id": "obj-919",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.fft~",
                "numoutlets": 3,
                "outlettype": [
                    "multichannelsignal",
                    "multichannelsignal",
                    "multichannelsignal",
                ],
                "patching_rect": [540.0, 1110.0, 45.0, 22.0],
                "id": "obj-920",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.filtercoeff~",
                "numoutlets": 5,
                "outlettype": [
                    "multichannelsignal",
                    "multichannelsignal",
                    "multichannelsignal",
                    "multichannelsignal",
                    "multichannelsignal",
                ],
                "patching_rect": [620.0, 1110.0, 83.0, 22.0],
                "id": "obj-921",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.frameaccum~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [700.0, 1110.0, 101.0, 22.0],
                "id": "obj-922",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.frameaverage~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [780.0, 1110.0, 109.0, 22.0],
                "id": "obj-923",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.framedelta~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [860.0, 1110.0, 92.0, 22.0],
                "id": "obj-924",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.framesmooth~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [940.0, 1110.0, 105.0, 22.0],
                "id": "obj-925",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.freqshift~",
                "numoutlets": 2,
                "outlettype": ["multichannelsignal", "multichannelsignal"],
                "patching_rect": [1020.0, 1110.0, 78.0, 22.0],
                "id": "obj-926",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.ftom~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [1100.0, 1110.0, 58.0, 22.0],
                "id": "obj-927",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.fzero~",
                "numoutlets": 4,
                "outlettype": ["", "", "", ""],
                "patching_rect": [1180.0, 1110.0, 62.0, 22.0],
                "id": "obj-928",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "gain~",
                "numoutlets": 2,
                "multichannelvariant": 1,
                "outlettype": ["multichannelsignal", ""],
                "patching_rect": [1260.0, 1110.0, 22.0, 140.0],
                "id": "obj-930",
                "numinlets": 1,
                "parameter_enable": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.gate~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [1340.0, 1110.0, 58.0, 22.0],
                "id": "obj-931",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.gen",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [1420.0, 1110.0, 48.0, 22.0],
                "id": "obj-932",
                "numinlets": 2,
                "data": {
                    "patcher": {
                        "fileversion": 1,
                        "appversion": {
                            "major": 8,
                            "minor": 6,
                            "revision": 0,
                            "architecture": "x64",
                            "modernui": 1,
                        },
                        "classnamespace": "dsp.gen",
                        "rect": [0.0, 0.0, 600.0, 450.0],
                        "bglocked": 0,
                        "openinpresentation": 0,
                        "default_fontsize": 12.0,
                        "default_fontface": 0,
                        "default_fontname": "Arial",
                        "gridonopen": 1,
                        "gridsize": [15.0, 15.0],
                        "gridsnaponopen": 1,
                        "objectsnaponopen": 1,
                        "statusbarvisible": 2,
                        "toolbarvisible": 1,
                        "lefttoolbarpinned": 0,
                        "toptoolbarpinned": 0,
                        "righttoolbarpinned": 0,
                        "bottomtoolbarpinned": 0,
                        "toolbars_unpinned_last_save": 0,
                        "tallnewobj": 0,
                        "boxanimatetime": 200,
                        "enablehscroll": 1,
                        "enablevscroll": 1,
                        "devicewidth": 0.0,
                        "description": "",
                        "digest": "",
                        "tags": "",
                        "style": "",
                        "subpatcher_template": "",
                        "assistshowspatchername": 0,
                        "boxes": [
                            {
                                "box": {
                                    "maxclass": "newobj",
                                    "text": "in 1",
                                    "numoutlets": 1,
                                    "outlettype": [""],
                                    "patching_rect": [50.0, 14.0, 28.0, 22.0],
                                    "id": "obj-1",
                                    "numinlets": 0,
                                }
                            },
                            {
                                "box": {
                                    "maxclass": "newobj",
                                    "text": "in 2",
                                    "numoutlets": 1,
                                    "outlettype": [""],
                                    "patching_rect": [305.0, 14.0, 28.0, 22.0],
                                    "id": "obj-2",
                                    "numinlets": 0,
                                }
                            },
                            {
                                "box": {
                                    "maxclass": "newobj",
                                    "text": "+",
                                    "numoutlets": 1,
                                    "outlettype": [""],
                                    "patching_rect": [176.0, 149.0, 29.5, 22.0],
                                    "id": "obj-3",
                                    "numinlets": 2,
                                }
                            },
                            {
                                "box": {
                                    "maxclass": "newobj",
                                    "text": "out 1",
                                    "numoutlets": 0,
                                    "patching_rect": [176.0, 418.0, 35.0, 22.0],
                                    "id": "obj-4",
                                    "numinlets": 1,
                                }
                            },
                        ],
                        "lines": [
                            {
                                "patchline": {
                                    "source": ["obj-3", 0],
                                    "destination": ["obj-4", 0],
                                }
                            },
                            {
                                "patchline": {
                                    "source": ["obj-2", 0],
                                    "destination": ["obj-3", 1],
                                }
                            },
                            {
                                "patchline": {
                                    "source": ["obj-1", 0],
                                    "destination": ["obj-3", 0],
                                }
                            },
                        ],
                    }
                },
                "wrapper_uniquekey": "u664013148",
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.generate~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [1500.0, 1110.0, 82.0, 22.0],
                "id": "obj-933",
                "numinlets": 4,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.gen~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [1580.0, 1110.0, 55.0, 22.0],
                "id": "obj-934",
                "numinlets": 2,
                "data": {
                    "patcher": {
                        "fileversion": 1,
                        "appversion": {
                            "major": 8,
                            "minor": 6,
                            "revision": 0,
                            "architecture": "x64",
                            "modernui": 1,
                        },
                        "classnamespace": "dsp.gen",
                        "rect": [0.0, 0.0, 600.0, 450.0],
                        "bglocked": 0,
                        "openinpresentation": 0,
                        "default_fontsize": 12.0,
                        "default_fontface": 0,
                        "default_fontname": "Arial",
                        "gridonopen": 1,
                        "gridsize": [15.0, 15.0],
                        "gridsnaponopen": 1,
                        "objectsnaponopen": 1,
                        "statusbarvisible": 2,
                        "toolbarvisible": 1,
                        "lefttoolbarpinned": 0,
                        "toptoolbarpinned": 0,
                        "righttoolbarpinned": 0,
                        "bottomtoolbarpinned": 0,
                        "toolbars_unpinned_last_save": 0,
                        "tallnewobj": 0,
                        "boxanimatetime": 200,
                        "enablehscroll": 1,
                        "enablevscroll": 1,
                        "devicewidth": 0.0,
                        "description": "",
                        "digest": "",
                        "tags": "",
                        "style": "",
                        "subpatcher_template": "",
                        "assistshowspatchername": 0,
                        "boxes": [
                            {
                                "box": {
                                    "maxclass": "newobj",
                                    "text": "in 1",
                                    "numoutlets": 1,
                                    "outlettype": [""],
                                    "patching_rect": [50.0, 14.0, 28.0, 22.0],
                                    "id": "obj-1",
                                    "numinlets": 0,
                                }
                            },
                            {
                                "box": {
                                    "maxclass": "newobj",
                                    "text": "in 2",
                                    "numoutlets": 1,
                                    "outlettype": [""],
                                    "patching_rect": [305.0, 14.0, 28.0, 22.0],
                                    "id": "obj-2",
                                    "numinlets": 0,
                                }
                            },
                            {
                                "box": {
                                    "maxclass": "newobj",
                                    "text": "+",
                                    "numoutlets": 1,
                                    "outlettype": [""],
                                    "patching_rect": [176.0, 149.0, 29.5, 22.0],
                                    "id": "obj-3",
                                    "numinlets": 2,
                                }
                            },
                            {
                                "box": {
                                    "maxclass": "newobj",
                                    "text": "out 1",
                                    "numoutlets": 0,
                                    "patching_rect": [176.0, 418.0, 35.0, 22.0],
                                    "id": "obj-4",
                                    "numinlets": 1,
                                }
                            },
                        ],
                        "lines": [
                            {
                                "patchline": {
                                    "source": ["obj-3", 0],
                                    "destination": ["obj-4", 0],
                                }
                            },
                            {
                                "patchline": {
                                    "source": ["obj-2", 0],
                                    "destination": ["obj-3", 1],
                                }
                            },
                            {
                                "patchline": {
                                    "source": ["obj-1", 0],
                                    "destination": ["obj-3", 0],
                                }
                            },
                        ],
                    }
                },
                "wrapper_uniquekey": "u470013165",
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.gradient~",
                "numoutlets": 3,
                "outlettype": ["multichannelsignal", "float", "list"],
                "patching_rect": [60.0, 1135.0, 78.0, 22.0],
                "id": "obj-935",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.greaterthaneq~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [140.0, 1135.0, 110.0, 22.0],
                "id": "obj-936",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.greaterthan~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [220.0, 1135.0, 96.0, 22.0],
                "id": "obj-937",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.groove~",
                "numoutlets": 2,
                "outlettype": ["multichannelsignal", "multichannelsignal"],
                "patching_rect": [300.0, 1135.0, 72.0, 22.0],
                "id": "obj-938",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.hilbert~",
                "numoutlets": 2,
                "outlettype": ["multichannelsignal", "multichannelsignal"],
                "patching_rect": [380.0, 1135.0, 68.0, 22.0],
                "id": "obj-939",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.ifft~",
                "numoutlets": 3,
                "outlettype": [
                    "multichannelsignal",
                    "multichannelsignal",
                    "multichannelsignal",
                ],
                "patching_rect": [460.0, 1135.0, 47.0, 22.0],
                "id": "obj-940",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.index~",
                "numoutlets": 0,
                "patching_rect": [540.0, 1135.0, 64.0, 22.0],
                "id": "obj-941",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.interleave~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [620.0, 1135.0, 87.0, 22.0],
                "id": "obj-942",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.in~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [700.0, 1135.0, 44.0, 22.0],
                "id": "obj-943",
                "numinlets": 1,
                "saved_object_attributes": {"attr_comment": ""},
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.kink~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [780.0, 1135.0, 56.0, 22.0],
                "id": "obj-944",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.lessthaneq~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [860.0, 1135.0, 93.0, 22.0],
                "id": "obj-945",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.lessthan~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [940.0, 1135.0, 80.0, 22.0],
                "id": "obj-946",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.limi~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [1020.0, 1135.0, 53.0, 22.0],
                "id": "obj-947",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.line~",
                "numoutlets": 3,
                "outlettype": ["multichannelsignal", "", ""],
                "patching_rect": [1100.0, 1135.0, 54.0, 22.0],
                "id": "obj-948",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.list~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [1180.0, 1135.0, 50.0, 22.0],
                "id": "obj-949",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.log~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [1260.0, 1135.0, 51.0, 22.0],
                "id": "obj-950",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.lookup~",
                "numoutlets": 0,
                "patching_rect": [1340.0, 1135.0, 70.0, 22.0],
                "id": "obj-951",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.lores~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [1420.0, 1135.0, 61.0, 22.0],
                "id": "obj-952",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.makelist",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [1500.0, 1135.0, 72.0, 22.0],
                "id": "obj-953",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.matrix~",
                "numoutlets": 4,
                "outlettype": ["multichannelsignal", "multichannelsignal", "", ""],
                "patching_rect": [1580.0, 1135.0, 68.0, 22.0],
                "id": "obj-954",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.maximum~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [60.0, 1160.0, 87.0, 22.0],
                "id": "obj-955",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.midiplayer~",
                "numoutlets": 2,
                "outlettype": ["signal", "midievent"],
                "patching_rect": [140.0, 1160.0, 90.0, 22.0],
                "id": "obj-956",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.minimum~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [220.0, 1160.0, 84.0, 22.0],
                "id": "obj-957",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.minmax~",
                "numoutlets": 5,
                "outlettype": ["multichannelsignal", "multichannelsignal", "", "", ""],
                "patching_rect": [300.0, 1160.0, 77.0, 22.0],
                "id": "obj-958",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.minus~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [380.0, 1160.0, 67.0, 22.0],
                "id": "obj-959",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.mixdown~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [460.0, 1160.0, 82.0, 22.0],
                "id": "obj-960",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.modulo~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [540.0, 1160.0, 74.0, 22.0],
                "id": "obj-961",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.mstosamps~",
                "numoutlets": 3,
                "outlettype": ["multichannelsignal", "", ""],
                "patching_rect": [620.0, 1160.0, 96.0, 22.0],
                "id": "obj-962",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.mtof~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [700.0, 1160.0, 58.0, 22.0],
                "id": "obj-963",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.noise~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [780.0, 1160.0, 64.0, 22.0],
                "id": "obj-964",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.normalize~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [860.0, 1160.0, 87.0, 22.0],
                "id": "obj-965",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.noteallocator~",
                "numoutlets": 6,
                "outlettype": ["list", "list", "int", "int", "", "int"],
                "patching_rect": [940.0, 1160.0, 104.0, 22.0],
                "id": "obj-966",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.notequals~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [1020.0, 1160.0, 87.0, 22.0],
                "id": "obj-967",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "mc.number~",
                "numoutlets": 3,
                "fontface": 0,
                "mode": 2,
                "outlettype": ["multichannelsignal", "float", "int"],
                "sig": 0.0,
                "patching_rect": [1100.0, 1160.0, 56.0, 34.0],
                "id": "obj-969",
                "fontsize": 12.0,
                "numinlets": 2,
                "fontname": "Arial",
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.omx.4band~",
                "numoutlets": 5,
                "outlettype": ["multichannelsignal", "multichannelsignal", "", "", ""],
                "patching_rect": [1180.0, 1160.0, 94.0, 22.0],
                "id": "obj-970",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.omx.5band~",
                "numoutlets": 5,
                "outlettype": ["multichannelsignal", "multichannelsignal", "", "", ""],
                "patching_rect": [1260.0, 1160.0, 94.0, 22.0],
                "id": "obj-971",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.omx.comp~",
                "numoutlets": 5,
                "outlettype": ["multichannelsignal", "multichannelsignal", "", "", ""],
                "patching_rect": [1340.0, 1160.0, 90.0, 22.0],
                "id": "obj-972",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.omx.peaklim~",
                "numoutlets": 5,
                "outlettype": ["multichannelsignal", "multichannelsignal", "", "", ""],
                "patching_rect": [1420.0, 1160.0, 102.0, 22.0],
                "id": "obj-973",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.onepole~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [1500.0, 1160.0, 78.0, 22.0],
                "id": "obj-974",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.op~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1580.0, 1160.0, 48.0, 22.0],
                "id": "obj-975",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.out~",
                "numoutlets": 0,
                "patching_rect": [60.0, 1185.0, 52.0, 22.0],
                "id": "obj-976",
                "numinlets": 1,
                "saved_object_attributes": {"attr_comment": ""},
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.overdrive~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [140.0, 1185.0, 84.0, 22.0],
                "id": "obj-977",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.pack~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [220.0, 1185.0, 60.0, 22.0],
                "id": "obj-978",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.pattern~",
                "numoutlets": 3,
                "outlettype": [
                    "multichannelsignal",
                    "multichannelsignal",
                    "dictionary",
                ],
                "patching_rect": [300.0, 1185.0, 72.0, 22.0],
                "id": "obj-979",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.peakamp~",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [380.0, 1185.0, 84.0, 22.0],
                "id": "obj-980",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.peek~",
                "numoutlets": 0,
                "patching_rect": [460.0, 1185.0, 61.0, 22.0],
                "id": "obj-981",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.pfft~",
                "numoutlets": 0,
                "patching_rect": [540.0, 1185.0, 51.0, 22.0],
                "id": "obj-982",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.phasegroove~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [620.0, 1185.0, 104.0, 22.0],
                "id": "obj-983",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.phaseshift~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [700.0, 1185.0, 90.0, 22.0],
                "id": "obj-984",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.phasewrap~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [780.0, 1185.0, 94.0, 22.0],
                "id": "obj-985",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.phasor~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [860.0, 1185.0, 72.0, 22.0],
                "id": "obj-986",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.pink~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [940.0, 1185.0, 57.0, 22.0],
                "id": "obj-987",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.pitchshift~",
                "numoutlets": 3,
                "outlettype": ["multichannelsignal", "", ""],
                "patching_rect": [1020.0, 1185.0, 82.0, 22.0],
                "id": "obj-988",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "mc.playlist~",
                "basictuning": 0,
                "pitchcorrection": 0,
                "numoutlets": 4,
                "originallength": [0],
                "mode": 0,
                "outlettype": ["multichannelsignal", "signal", "", "dictionary"],
                "followglobaltempo": 0,
                "patching_rect": [1100.0, 1185.0, 150.0, 92.0],
                "id": "obj-990",
                "formantcorrection": 0,
                "timestretch": [0],
                "originaltempo": 0,
                "quality": 0,
                "numinlets": 1,
                "parameter_enable": 0,
                "data": {"clips": []},
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.play~",
                "numoutlets": 3,
                "outlettype": ["multichannelsignal", "", ""],
                "patching_rect": [1180.0, 1185.0, 57.0, 22.0],
                "id": "obj-991",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.plusequals~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [1260.0, 1185.0, 92.0, 22.0],
                "id": "obj-992",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.plus~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [1340.0, 1185.0, 57.0, 22.0],
                "id": "obj-993",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.poltocar~",
                "numoutlets": 2,
                "outlettype": ["multichannelsignal", "multichannelsignal"],
                "patching_rect": [1420.0, 1185.0, 78.0, 22.0],
                "id": "obj-994",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.poly~",
                "numoutlets": 0,
                "patching_rect": [1500.0, 1185.0, 57.0, 22.0],
                "id": "obj-995",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.pong~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [1580.0, 1185.0, 62.0, 22.0],
                "id": "obj-996",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.pow~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [60.0, 1210.0, 57.0, 22.0],
                "id": "obj-997",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.rampsmooth~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [140.0, 1210.0, 102.0, 22.0],
                "id": "obj-998",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.ramp~",
                "numoutlets": 3,
                "outlettype": ["multichannelsignal", "", ""],
                "patching_rect": [220.0, 1210.0, 62.0, 22.0],
                "id": "obj-999",
                "numinlets": 4,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.rand~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [300.0, 1210.0, 59.0, 22.0],
                "id": "obj-1000",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.range~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [380.0, 1210.0, 66.0, 22.0],
                "id": "obj-1001",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.rate~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [460.0, 1210.0, 56.0, 22.0],
                "id": "obj-1002",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.rdiv~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [540.0, 1210.0, 54.0, 22.0],
                "id": "obj-1003",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.receive~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [620.0, 1210.0, 74.0, 22.0],
                "id": "obj-1004",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.record~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [700.0, 1210.0, 69.0, 22.0],
                "id": "obj-1005",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.rect~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [780.0, 1210.0, 55.0, 22.0],
                "id": "obj-1006",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.resize~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [860.0, 1210.0, 67.0, 22.0],
                "id": "obj-1007",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.reson~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [940.0, 1210.0, 65.0, 22.0],
                "id": "obj-1008",
                "numinlets": 4,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.retune~",
                "numoutlets": 6,
                "outlettype": [
                    "multichannelsignal",
                    "multichannelsignal",
                    "multichannelsignal",
                    "multichannelsignal",
                    "",
                    "",
                ],
                "patching_rect": [1020.0, 1210.0, 69.0, 22.0],
                "id": "obj-1009",
                "numinlets": 3,
                "saved_object_attributes": {
                    "notebase": 0,
                    "notelist": [
                        100,
                        200,
                        300,
                        400,
                        500,
                        600,
                        700,
                        800,
                        900,
                        1000,
                        1100,
                    ],
                    "pitchdetection": 0,
                    "retune": 1,
                    "use_16bit": [0],
                },
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.rminus~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [1100.0, 1210.0, 71.0, 22.0],
                "id": "obj-1010",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.round~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [1180.0, 1210.0, 66.0, 22.0],
                "id": "obj-1011",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.route",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [1260.0, 1210.0, 55.0, 22.0],
                "id": "obj-1012",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.sah~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [1340.0, 1210.0, 54.0, 22.0],
                "id": "obj-1013",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.sampstoms~",
                "numoutlets": 3,
                "outlettype": ["multichannelsignal", "", ""],
                "patching_rect": [1420.0, 1210.0, 96.0, 22.0],
                "id": "obj-1014",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.sash~",
                "numoutlets": 0,
                "patching_rect": [1500.0, 1210.0, 60.0, 22.0],
                "id": "obj-1015",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.saw~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [1580.0, 1210.0, 56.0, 22.0],
                "id": "obj-1016",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.scale~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [60.0, 1235.0, 63.0, 22.0],
                "id": "obj-1017",
                "numinlets": 6,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.selector~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [140.0, 1235.0, 77.0, 22.0],
                "id": "obj-1018",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.send~",
                "numoutlets": 0,
                "patching_rect": [220.0, 1235.0, 61.0, 22.0],
                "id": "obj-1019",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.separate~",
                "numoutlets": 2,
                "outlettype": ["multichannelsignal", "multichannelsignal"],
                "patching_rect": [300.0, 1235.0, 82.0, 22.0],
                "id": "obj-1020",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.seq~",
                "numoutlets": 4,
                "outlettype": ["", "", "", ""],
                "patching_rect": [380.0, 1235.0, 54.0, 22.0],
                "id": "obj-1021",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.sfplay~",
                "numoutlets": 2,
                "outlettype": ["multichannelsignal", "bang"],
                "patching_rect": [460.0, 1235.0, 66.0, 22.0],
                "id": "obj-1022",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.sfrecord~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [540.0, 1235.0, 78.0, 22.0],
                "id": "obj-1023",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.shape~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [620.0, 1235.0, 68.0, 22.0],
                "id": "obj-1024",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.sig~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [700.0, 1235.0, 50.0, 22.0],
                "id": "obj-1025",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.sinh~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [780.0, 1235.0, 57.0, 22.0],
                "id": "obj-1026",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.sinx~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [860.0, 1235.0, 56.0, 22.0],
                "id": "obj-1027",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.slide~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [940.0, 1235.0, 60.0, 22.0],
                "id": "obj-1028",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.snapshot~",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [1020.0, 1235.0, 84.0, 22.0],
                "id": "obj-1029",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.snowfall~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [1100.0, 1235.0, 78.0, 22.0],
                "id": "obj-1030",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.snowphasor~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [1180.0, 1235.0, 100.0, 22.0],
                "id": "obj-1031",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.spike~",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [1260.0, 1235.0, 63.0, 22.0],
                "id": "obj-1032",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.sqrt~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [1340.0, 1235.0, 55.0, 22.0],
                "id": "obj-1033",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.stash~",
                "numoutlets": 2,
                "outlettype": ["multichannelsignal", "multichannelsignal"],
                "patching_rect": [1420.0, 1235.0, 64.0, 22.0],
                "id": "obj-1034",
                "numinlets": 4,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.stereo~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [1500.0, 1235.0, 68.0, 22.0],
                "id": "obj-1035",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.stutter~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [1580.0, 1235.0, 68.0, 22.0],
                "id": "obj-1036",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.subdiv~",
                "numoutlets": 4,
                "outlettype": ["multichannelsignal", "multichannelsignal", "", ""],
                "patching_rect": [60.0, 1260.0, 70.0, 22.0],
                "id": "obj-1037",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.svf~",
                "numoutlets": 4,
                "outlettype": [
                    "multichannelsignal",
                    "multichannelsignal",
                    "multichannelsignal",
                    "multichannelsignal",
                ],
                "patching_rect": [140.0, 1260.0, 50.0, 22.0],
                "id": "obj-1038",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.swing~",
                "numoutlets": 4,
                "outlettype": ["multichannelsignal", "multichannelsignal", "", ""],
                "patching_rect": [220.0, 1260.0, 66.0, 22.0],
                "id": "obj-1039",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.sync~",
                "numoutlets": 4,
                "outlettype": ["multichannelsignal", "", "", ""],
                "patching_rect": [300.0, 1260.0, 60.0, 22.0],
                "id": "obj-1040",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.table~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [380.0, 1260.0, 61.0, 22.0],
                "id": "obj-1041",
                "numinlets": 1,
                "saved_object_attributes": {
                    "embed": 0,
                    "name": "",
                    "parameter_enable": 0,
                    "parameter_mappable": 0,
                    "range": 128,
                    "size": 128,
                },
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.tanh~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [460.0, 1260.0, 58.0, 22.0],
                "id": "obj-1042",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.tanx~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [540.0, 1260.0, 58.0, 22.0],
                "id": "obj-1043",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.tapin~",
                "numoutlets": 1,
                "outlettype": ["tapconnect"],
                "patching_rect": [620.0, 1260.0, 61.0, 22.0],
                "id": "obj-1044",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.tapout~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [700.0, 1260.0, 68.0, 22.0],
                "id": "obj-1045",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.target",
                "numoutlets": 2,
                "outlettype": ["setvalue", "int"],
                "patching_rect": [780.0, 1260.0, 59.0, 22.0],
                "id": "obj-1046",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.targetlist",
                "numoutlets": 2,
                "outlettype": ["setvalue", "int"],
                "patching_rect": [860.0, 1260.0, 73.0, 22.0],
                "id": "obj-1047",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.teeth~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [940.0, 1260.0, 62.0, 22.0],
                "id": "obj-1048",
                "numinlets": 6,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.thresh~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [1020.0, 1260.0, 68.0, 22.0],
                "id": "obj-1049",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.times~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [1100.0, 1260.0, 64.0, 22.0],
                "id": "obj-1050",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.train~",
                "numoutlets": 3,
                "outlettype": ["multichannelsignal", "", ""],
                "patching_rect": [1180.0, 1260.0, 58.0, 22.0],
                "id": "obj-1051",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.transpose~",
                "numoutlets": 2,
                "outlettype": ["multichannelsignal", "multichannelsignal"],
                "patching_rect": [1260.0, 1260.0, 88.0, 22.0],
                "id": "obj-1052",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.trapezoid~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [1340.0, 1260.0, 84.0, 22.0],
                "id": "obj-1053",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.triangle~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [1420.0, 1260.0, 74.0, 22.0],
                "id": "obj-1054",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.tri~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [1500.0, 1260.0, 45.0, 22.0],
                "id": "obj-1055",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.trunc~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [1580.0, 1260.0, 62.0, 22.0],
                "id": "obj-1056",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.twist~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [60.0, 1285.0, 59.0, 22.0],
                "id": "obj-1057",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.unpack~",
                "numoutlets": 2,
                "outlettype": ["signal", "signal"],
                "patching_rect": [140.0, 1285.0, 74.0, 22.0],
                "id": "obj-1058",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.updown~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [220.0, 1285.0, 77.0, 22.0],
                "id": "obj-1059",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.vectral~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [300.0, 1285.0, 70.0, 22.0],
                "id": "obj-1060",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.voiceallocator~",
                "numoutlets": 2,
                "outlettype": ["", "int"],
                "patching_rect": [380.0, 1285.0, 108.0, 22.0],
                "id": "obj-1061",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "viewvisibility": 0,
                "offset": [0.0, 0.0],
                "lockeddragscroll": 0,
                "clickthrough": 0,
                "enablehscroll": 0,
                "enablevscroll": 0,
                "lockedsize": 0,
                "bgmode": 0,
                "border": 0,
                "text": "mc.vst~",
                "numoutlets": 9,
                "outlettype": [
                    "multichannelsignal",
                    "multichannelsignal",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                ],
                "patching_rect": [460.0, 1285.0, 50.0, 22.0],
                "id": "obj-1062",
                "numinlets": 2,
                "data": {"autosave": 1},
                "saved_object_attributes": {
                    "parameter_enable": 1,
                    "parameter_mappable": 0,
                },
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.wave~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [540.0, 1285.0, 63.0, 22.0],
                "id": "obj-1063",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.what~",
                "numoutlets": 3,
                "outlettype": ["multichannelsignal", "", ""],
                "patching_rect": [620.0, 1285.0, 60.0, 22.0],
                "id": "obj-1064",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.where~",
                "numoutlets": 2,
                "outlettype": ["multichannelsignal", "multichannelsignal"],
                "patching_rect": [700.0, 1285.0, 68.0, 22.0],
                "id": "obj-1065",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.zerox~",
                "numoutlets": 2,
                "outlettype": ["multichannelsignal", "multichannelsignal"],
                "patching_rect": [780.0, 1285.0, 64.0, 22.0],
                "id": "obj-1066",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mc.zigzag~",
                "numoutlets": 5,
                "outlettype": ["multichannelsignal", "multichannelsignal", "", "", ""],
                "patching_rect": [860.0, 1285.0, 70.0, 22.0],
                "id": "obj-1067",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mcs.2d.wave~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [940.0, 1285.0, 86.0, 22.0],
                "id": "obj-1068",
                "numinlets": 4,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "varname": "amxd~[2]",
                "viewvisibility": 0,
                "offset": [0.0, 0.0],
                "lockeddragscroll": 0,
                "clickthrough": 0,
                "enablehscroll": 0,
                "enablevscroll": 0,
                "lockedsize": 0,
                "bgmode": 1,
                "border": 0,
                "text": "mcs.amxd~",
                "numoutlets": 3,
                "outlettype": ["multichannelsignal", "", ""],
                "patching_rect": [1020.0, 1285.0, 70.0, 22.0],
                "id": "obj-1069",
                "numinlets": 2,
                "autosave": 1,
                "saved_object_attributes": {
                    "parameter_enable": 1,
                    "patchername": "",
                    "patchername_fallback": "/Volumes/<none>/",
                },
                "saved_attribute_attributes": {
                    "valueof": {
                        "parameter_invisible": 1,
                        "parameter_longname": "amxd~[5]",
                        "parameter_shortname": "amxd~[5]",
                        "parameter_type": 3,
                    }
                },
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mcs.fffb~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [1100.0, 1285.0, 57.0, 22.0],
                "id": "obj-1070",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mcs.gate~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [1180.0, 1285.0, 64.0, 22.0],
                "id": "obj-1071",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mcs.gen~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [1260.0, 1285.0, 61.0, 22.0],
                "id": "obj-1072",
                "numinlets": 1,
                "patcher": {
                    "fileversion": 1,
                    "appversion": {
                        "major": 8,
                        "minor": 6,
                        "revision": 0,
                        "architecture": "x64",
                        "modernui": 1,
                    },
                    "classnamespace": "dsp.gen",
                    "rect": [0.0, 0.0, 600.0, 450.0],
                    "bglocked": 0,
                    "openinpresentation": 0,
                    "default_fontsize": 12.0,
                    "default_fontface": 0,
                    "default_fontname": "Arial",
                    "gridonopen": 1,
                    "gridsize": [15.0, 15.0],
                    "gridsnaponopen": 1,
                    "objectsnaponopen": 1,
                    "statusbarvisible": 2,
                    "toolbarvisible": 1,
                    "lefttoolbarpinned": 0,
                    "toptoolbarpinned": 0,
                    "righttoolbarpinned": 0,
                    "bottomtoolbarpinned": 0,
                    "toolbars_unpinned_last_save": 0,
                    "tallnewobj": 0,
                    "boxanimatetime": 200,
                    "enablehscroll": 1,
                    "enablevscroll": 1,
                    "devicewidth": 0.0,
                    "description": "",
                    "digest": "",
                    "tags": "",
                    "style": "",
                    "subpatcher_template": "",
                    "assistshowspatchername": 0,
                    "boxes": [
                        {
                            "box": {
                                "maxclass": "newobj",
                                "text": "in 1",
                                "numoutlets": 1,
                                "outlettype": [""],
                                "patching_rect": [50.0, 14.0, 28.0, 22.0],
                                "id": "obj-1",
                                "numinlets": 0,
                            }
                        },
                        {
                            "box": {
                                "maxclass": "newobj",
                                "text": "in 2",
                                "numoutlets": 1,
                                "outlettype": [""],
                                "patching_rect": [305.0, 14.0, 28.0, 22.0],
                                "id": "obj-2",
                                "numinlets": 0,
                            }
                        },
                        {
                            "box": {
                                "maxclass": "newobj",
                                "text": "+",
                                "numoutlets": 1,
                                "outlettype": [""],
                                "patching_rect": [176.0, 149.0, 29.5, 22.0],
                                "id": "obj-3",
                                "numinlets": 2,
                            }
                        },
                        {
                            "box": {
                                "maxclass": "newobj",
                                "text": "out 1",
                                "numoutlets": 0,
                                "patching_rect": [176.0, 418.0, 35.0, 22.0],
                                "id": "obj-4",
                                "numinlets": 1,
                            }
                        },
                    ],
                    "lines": [
                        {
                            "patchline": {
                                "source": ["obj-3", 0],
                                "destination": ["obj-4", 0],
                            }
                        },
                        {
                            "patchline": {
                                "source": ["obj-2", 0],
                                "destination": ["obj-3", 1],
                            }
                        },
                        {
                            "patchline": {
                                "source": ["obj-1", 0],
                                "destination": ["obj-3", 0],
                            }
                        },
                    ],
                },
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mcs.groove~",
                "numoutlets": 2,
                "outlettype": ["multichannelsignal", "signal"],
                "patching_rect": [1340.0, 1285.0, 78.0, 22.0],
                "id": "obj-1073",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mcs.limi~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [1420.0, 1285.0, 59.0, 22.0],
                "id": "obj-1074",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mcs.matrix~",
                "numoutlets": 2,
                "outlettype": ["multichannelsignal", ""],
                "patching_rect": [1500.0, 1285.0, 74.0, 22.0],
                "id": "obj-1075",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mcs.play~",
                "numoutlets": 2,
                "outlettype": ["multichannelsignal", "bang"],
                "patching_rect": [1580.0, 1285.0, 63.0, 22.0],
                "id": "obj-1076",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mcs.poly~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [60.0, 1310.0, 63.0, 22.0],
                "id": "obj-1077",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mcs.selector~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [140.0, 1310.0, 83.0, 22.0],
                "id": "obj-1078",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mcs.sig~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [220.0, 1310.0, 56.0, 22.0],
                "id": "obj-1079",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mcs.tapout~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [300.0, 1310.0, 74.0, 22.0],
                "id": "obj-1080",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "varname": "mcs.vst~",
                "viewvisibility": 0,
                "offset": [0.0, 0.0],
                "lockeddragscroll": 0,
                "clickthrough": 0,
                "enablehscroll": 0,
                "enablevscroll": 0,
                "lockedsize": 0,
                "bgmode": 0,
                "border": 0,
                "text": "mcs.vst~",
                "numoutlets": 7,
                "outlettype": ["multichannelsignal", "", "list", "int", "", "", ""],
                "patching_rect": [380.0, 1310.0, 56.0, 22.0],
                "id": "obj-1081",
                "numinlets": 1,
                "save": ["#N", "mcs.vst~", "loaduniqueid", 0, ";"],
                "autosave": 1,
                "saved_object_attributes": {
                    "parameter_enable": 1,
                    "parameter_mappable": 0,
                },
                "saved_attribute_attributes": {
                    "valueof": {
                        "parameter_invisible": 1,
                        "parameter_longname": "mcs.vst~",
                        "parameter_shortname": "mcs.vst~",
                        "parameter_type": 3,
                    }
                },
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mcs.wave~",
                "numoutlets": 1,
                "outlettype": ["multichannelsignal"],
                "patching_rect": [460.0, 1310.0, 69.0, 22.0],
                "id": "obj-1082",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mcwrapper-group",
                "numoutlets": 0,
                "patching_rect": [540.0, 1310.0, 103.0, 22.0],
                "id": "obj-1083",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "meter~",
                "numoutlets": 1,
                "outlettype": ["float"],
                "patching_rect": [620.0, 1310.0, 80.0, 13.0],
                "id": "obj-1085",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "minimum~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [700.0, 1310.0, 64.0, 22.0],
                "id": "obj-1086",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "minmax~",
                "numoutlets": 4,
                "outlettype": ["signal", "signal", "float", "float"],
                "patching_rect": [780.0, 1310.0, 58.0, 22.0],
                "id": "obj-1087",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "minus~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [860.0, 1310.0, 48.0, 22.0],
                "id": "obj-1088",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "modulo~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [940.0, 1310.0, 55.0, 22.0],
                "id": "obj-1089",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mstosamps~",
                "numoutlets": 2,
                "outlettype": ["signal", "float"],
                "patching_rect": [1020.0, 1310.0, 77.0, 22.0],
                "id": "obj-1090",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mtof~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1100.0, 1310.0, 39.0, 22.0],
                "id": "obj-1091",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mute~",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [1180.0, 1310.0, 42.0, 22.0],
                "id": "obj-1092",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "mxj~",
                "numoutlets": 0,
                "patching_rect": [1260.0, 1310.0, 34.0, 22.0],
                "id": "obj-1093",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "noise~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1340.0, 1310.0, 44.0, 22.0],
                "id": "obj-1094",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "normalize~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1420.0, 1310.0, 68.0, 22.0],
                "id": "obj-1095",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "notequals~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1500.0, 1310.0, 68.0, 22.0],
                "id": "obj-1096",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "number~",
                "numoutlets": 2,
                "fontface": 0,
                "mode": 2,
                "outlettype": ["signal", "float"],
                "sig": 0.0,
                "patching_rect": [1580.0, 1310.0, 56.0, 22.0],
                "id": "obj-1098",
                "fontsize": 12.0,
                "numinlets": 2,
                "fontname": "Arial",
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "omx.4band~",
                "numoutlets": 4,
                "outlettype": ["signal", "signal", "list", "list"],
                "patching_rect": [60.0, 1335.0, 75.0, 22.0],
                "id": "obj-1099",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "omx.5band~",
                "numoutlets": 4,
                "outlettype": ["signal", "signal", "list", "list"],
                "patching_rect": [140.0, 1335.0, 75.0, 22.0],
                "id": "obj-1100",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "omx.comp~",
                "numoutlets": 4,
                "outlettype": ["signal", "signal", "list", "list"],
                "patching_rect": [220.0, 1335.0, 71.0, 22.0],
                "id": "obj-1101",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "omx.peaklim~",
                "numoutlets": 4,
                "outlettype": ["signal", "signal", "list", "list"],
                "patching_rect": [300.0, 1335.0, 83.0, 22.0],
                "id": "obj-1102",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "onepole~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [380.0, 1335.0, 58.0, 22.0],
                "id": "obj-1103",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "oscbank~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [460.0, 1335.0, 60.0, 22.0],
                "id": "obj-1104",
                "numinlets": 4,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "out",
                "numoutlets": 0,
                "patching_rect": [540.0, 1335.0, 25.0, 22.0],
                "id": "obj-1105",
                "numinlets": 1,
                "saved_object_attributes": {"attr_comment": ""},
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "out~",
                "numoutlets": 0,
                "patching_rect": [620.0, 1335.0, 32.0, 22.0],
                "id": "obj-1106",
                "numinlets": 1,
                "saved_object_attributes": {"attr_comment": ""},
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "overdrive~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [700.0, 1335.0, 65.0, 22.0],
                "id": "obj-1107",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "pass~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [780.0, 1335.0, 41.0, 22.0],
                "id": "obj-1108",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "peakamp~",
                "numoutlets": 1,
                "outlettype": ["float"],
                "patching_rect": [860.0, 1335.0, 65.0, 22.0],
                "id": "obj-1109",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "peek~",
                "numoutlets": 0,
                "patching_rect": [940.0, 1335.0, 42.0, 22.0],
                "id": "obj-1110",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "pfft~",
                "numoutlets": 0,
                "patching_rect": [1020.0, 1335.0, 32.0, 22.0],
                "id": "obj-1111",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "phasegroove~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1100.0, 1335.0, 85.0, 22.0],
                "id": "obj-1112",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "phaseshift~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1180.0, 1335.0, 70.0, 22.0],
                "id": "obj-1113",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "phasewrap~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1260.0, 1335.0, 74.0, 22.0],
                "id": "obj-1114",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "phasor~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1340.0, 1335.0, 52.0, 22.0],
                "id": "obj-1115",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "pink~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1420.0, 1335.0, 38.0, 22.0],
                "id": "obj-1116",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "pitchshift~",
                "numoutlets": 2,
                "outlettype": ["signal", ""],
                "patching_rect": [1500.0, 1335.0, 63.0, 22.0],
                "id": "obj-1117",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "playlist~",
                "basictuning": 0,
                "pitchcorrection": 0,
                "numoutlets": 5,
                "originallength": [0],
                "mode": 0,
                "outlettype": ["signal", "signal", "signal", "", "dictionary"],
                "followglobaltempo": 0,
                "patching_rect": [1580.0, 1335.0, 150.0, 92.0],
                "id": "obj-1119",
                "formantcorrection": 0,
                "timestretch": [0],
                "originaltempo": 0,
                "quality": 0,
                "numinlets": 1,
                "parameter_enable": 0,
                "data": {"clips": []},
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "play~",
                "numoutlets": 2,
                "outlettype": ["signal", "bang"],
                "patching_rect": [60.0, 1360.0, 38.0, 22.0],
                "id": "obj-1120",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "plot~",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [140.0, 1360.0, 50.0, 50.0],
                "id": "obj-1122",
                "numinlets": 1,
                "subplots": [
                    {
                        "color": [0.4, 0.4, 0.75, 1.0],
                        "thickness": 3.0,
                        "point_style": "circle",
                        "line_style": "origin",
                        "number_style": "none",
                        "filter": "none",
                        "domain_start": 0.0,
                        "domain_end": 1.0,
                        "domain_style": "linear",
                        "domain_markers": [],
                        "domain_labels": [],
                        "range_start": 0.0,
                        "range_end": 1.0,
                        "range_style": "linear",
                        "range_markers": [],
                        "range_labels": [],
                        "origin_x": 0.0,
                        "origin_y": 0.0,
                    }
                ],
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "plugin~",
                "numoutlets": 2,
                "outlettype": ["signal", "signal"],
                "patching_rect": [220.0, 1360.0, 48.0, 22.0],
                "id": "obj-1123",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "plugout~",
                "numoutlets": 2,
                "outlettype": ["signal", "signal"],
                "patching_rect": [300.0, 1360.0, 55.0, 22.0],
                "id": "obj-1124",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "plugphasor~",
                "numoutlets": 2,
                "outlettype": ["signal", "list"],
                "patching_rect": [380.0, 1360.0, 75.0, 22.0],
                "id": "obj-1125",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "plugreceive~",
                "numoutlets": 0,
                "patching_rect": [460.0, 1360.0, 77.0, 22.0],
                "id": "obj-1126",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "plugsend~",
                "numoutlets": 0,
                "patching_rect": [540.0, 1360.0, 64.0, 22.0],
                "id": "obj-1127",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "plugsync~",
                "numoutlets": 9,
                "outlettype": [
                    "int",
                    "int",
                    "int",
                    "float",
                    "list",
                    "float",
                    "float",
                    "int",
                    "int",
                ],
                "patching_rect": [620.0, 1360.0, 63.0, 22.0],
                "id": "obj-1128",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "plusequals~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [700.0, 1360.0, 73.0, 22.0],
                "id": "obj-1129",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "plus~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [780.0, 1360.0, 38.0, 22.0],
                "id": "obj-1130",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "poke~",
                "numoutlets": 0,
                "patching_rect": [860.0, 1360.0, 42.0, 22.0],
                "id": "obj-1131",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "poltocar~",
                "numoutlets": 2,
                "outlettype": ["signal", "signal"],
                "patching_rect": [940.0, 1360.0, 58.0, 22.0],
                "id": "obj-1132",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "polybuffer~",
                "numoutlets": 0,
                "patching_rect": [1020.0, 1360.0, 68.0, 22.0],
                "id": "obj-1133",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "poly~",
                "numoutlets": 0,
                "patching_rect": [1100.0, 1360.0, 38.0, 22.0],
                "id": "obj-1134",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "pong~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1180.0, 1360.0, 42.0, 22.0],
                "id": "obj-1135",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "pow~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1260.0, 1360.0, 38.0, 22.0],
                "id": "obj-1136",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "rampsmooth~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1340.0, 1360.0, 82.0, 22.0],
                "id": "obj-1137",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "ramp~",
                "numoutlets": 2,
                "outlettype": ["signal", "bang"],
                "patching_rect": [1420.0, 1360.0, 43.0, 22.0],
                "id": "obj-1138",
                "numinlets": 4,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "rand~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1500.0, 1360.0, 40.0, 22.0],
                "id": "obj-1139",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "rate~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1580.0, 1360.0, 36.0, 22.0],
                "id": "obj-1140",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "rdiv~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [60.0, 1385.0, 35.0, 22.0],
                "id": "obj-1141",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "receive~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [140.0, 1385.0, 54.0, 22.0],
                "id": "obj-1142",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "record~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [220.0, 1385.0, 50.0, 22.0],
                "id": "obj-1143",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "rect~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [300.0, 1385.0, 36.0, 22.0],
                "id": "obj-1144",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "reson~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [380.0, 1385.0, 46.0, 22.0],
                "id": "obj-1145",
                "numinlets": 4,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "retune~",
                "numoutlets": 5,
                "outlettype": ["signal", "signal", "signal", "signal", "list"],
                "patching_rect": [460.0, 1385.0, 50.0, 22.0],
                "id": "obj-1146",
                "numinlets": 3,
                "saved_object_attributes": {
                    "notebase": 0,
                    "notelist": [
                        100,
                        200,
                        300,
                        400,
                        500,
                        600,
                        700,
                        800,
                        900,
                        1000,
                        1100,
                    ],
                    "pitchdetection": 0,
                    "retune": 1,
                    "use_16bit": [0],
                },
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "rewire~",
                "numoutlets": 6,
                "outlettype": ["signal", "signal", "", "", "", ""],
                "patching_rect": [540.0, 1385.0, 48.0, 22.0],
                "id": "obj-1147",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "rminus~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [620.0, 1385.0, 52.0, 22.0],
                "id": "obj-1148",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "round~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [700.0, 1385.0, 46.0, 22.0],
                "id": "obj-1149",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "sah~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [780.0, 1385.0, 35.0, 22.0],
                "id": "obj-1150",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "sampstoms~",
                "numoutlets": 2,
                "outlettype": ["signal", "float"],
                "patching_rect": [860.0, 1385.0, 77.0, 22.0],
                "id": "obj-1151",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "sash~",
                "numoutlets": 0,
                "patching_rect": [940.0, 1385.0, 41.0, 22.0],
                "id": "obj-1152",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "saw~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1020.0, 1385.0, 37.0, 22.0],
                "id": "obj-1153",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "scale~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1100.0, 1385.0, 44.0, 22.0],
                "id": "obj-1154",
                "numinlets": 6,
            }
        },
        {
            "box": {
                "maxclass": "scope~",
                "numoutlets": 0,
                "patching_rect": [1180.0, 1385.0, 130.0, 130.0],
                "id": "obj-1156",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "selector~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1260.0, 1385.0, 58.0, 22.0],
                "id": "obj-1157",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "send~",
                "numoutlets": 0,
                "patching_rect": [1340.0, 1385.0, 42.0, 22.0],
                "id": "obj-1158",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "seq~",
                "numoutlets": 3,
                "outlettype": ["", "", ""],
                "patching_rect": [1420.0, 1385.0, 35.0, 22.0],
                "id": "obj-1159",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "sfinfo~",
                "numoutlets": 6,
                "outlettype": ["int", "int", "float", "float", "", ""],
                "patching_rect": [1500.0, 1385.0, 44.0, 22.0],
                "id": "obj-1160",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "sflist~",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [1580.0, 1385.0, 40.0, 22.0],
                "id": "obj-1161",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "sfplay~",
                "numoutlets": 2,
                "outlettype": ["signal", "bang"],
                "patching_rect": [60.0, 1410.0, 47.0, 22.0],
                "id": "obj-1162",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "sfrecord~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [140.0, 1410.0, 59.0, 22.0],
                "id": "obj-1163",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "shape~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [220.0, 1410.0, 48.0, 22.0],
                "id": "obj-1164",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "sig~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [300.0, 1410.0, 31.0, 22.0],
                "id": "obj-1165",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "sinh~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [380.0, 1410.0, 38.0, 22.0],
                "id": "obj-1166",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "sinx~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [460.0, 1410.0, 37.0, 22.0],
                "id": "obj-1167",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "slide~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [540.0, 1410.0, 40.0, 22.0],
                "id": "obj-1168",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "snapshot-group",
                "numoutlets": 0,
                "patching_rect": [620.0, 1410.0, 92.0, 22.0],
                "id": "obj-1169",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "snapshot~",
                "numoutlets": 1,
                "outlettype": ["float"],
                "patching_rect": [700.0, 1410.0, 64.0, 22.0],
                "id": "obj-1170",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "snowfall~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [780.0, 1410.0, 59.0, 22.0],
                "id": "obj-1171",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "spectroscope~",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [860.0, 1410.0, 300.0, 100.0],
                "id": "obj-1173",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "spike~",
                "numoutlets": 1,
                "outlettype": ["float"],
                "patching_rect": [940.0, 1410.0, 44.0, 22.0],
                "id": "obj-1174",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "sqrt~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1020.0, 1410.0, 36.0, 22.0],
                "id": "obj-1175",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "stash~",
                "numoutlets": 2,
                "outlettype": ["signal", "signal"],
                "patching_rect": [1100.0, 1410.0, 44.0, 22.0],
                "id": "obj-1176",
                "numinlets": 4,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "stretch~",
                "numoutlets": 0,
                "patching_rect": [1180.0, 1410.0, 52.0, 22.0],
                "id": "obj-1177",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "stutter~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1260.0, 1410.0, 49.0, 22.0],
                "id": "obj-1178",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "subdiv~",
                "numoutlets": 3,
                "outlettype": ["signal", "signal", "int"],
                "patching_rect": [1340.0, 1410.0, 50.0, 22.0],
                "id": "obj-1179",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "svf~",
                "numoutlets": 4,
                "outlettype": ["signal", "signal", "signal", "signal"],
                "patching_rect": [1420.0, 1410.0, 31.0, 22.0],
                "id": "obj-1180",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "swing~",
                "numoutlets": 3,
                "outlettype": ["signal", "signal", "int"],
                "patching_rect": [1500.0, 1410.0, 46.0, 22.0],
                "id": "obj-1181",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "sync~",
                "numoutlets": 3,
                "outlettype": ["signal", "", "int"],
                "patching_rect": [1580.0, 1410.0, 40.0, 22.0],
                "id": "obj-1182",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "table~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [60.0, 1435.0, 42.0, 22.0],
                "id": "obj-1183",
                "numinlets": 1,
                "saved_object_attributes": {
                    "embed": 0,
                    "name": "",
                    "parameter_enable": 0,
                    "parameter_mappable": 0,
                    "range": 128,
                    "size": 128,
                },
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "tanh~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [140.0, 1435.0, 39.0, 22.0],
                "id": "obj-1184",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "tanx~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [220.0, 1435.0, 38.0, 22.0],
                "id": "obj-1185",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "tapin~",
                "numoutlets": 1,
                "outlettype": ["tapconnect"],
                "patching_rect": [300.0, 1435.0, 42.0, 22.0],
                "id": "obj-1186",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "tapout~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [380.0, 1435.0, 49.0, 22.0],
                "id": "obj-1187",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "techno~",
                "numoutlets": 3,
                "outlettype": ["signal", "signal", "signal"],
                "patching_rect": [460.0, 1435.0, 52.0, 22.0],
                "id": "obj-1188",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "teeth~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [540.0, 1435.0, 42.0, 22.0],
                "id": "obj-1189",
                "numinlets": 6,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "thispoly~",
                "numoutlets": 3,
                "outlettype": ["int", "int", "int"],
                "patching_rect": [620.0, 1435.0, 56.0, 22.0],
                "id": "obj-1190",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "thresh~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [700.0, 1435.0, 49.0, 22.0],
                "id": "obj-1191",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "times~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [780.0, 1435.0, 44.0, 22.0],
                "id": "obj-1192",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "train~",
                "numoutlets": 2,
                "outlettype": ["signal", "bang"],
                "patching_rect": [860.0, 1435.0, 39.0, 22.0],
                "id": "obj-1193",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "trapezoid~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [940.0, 1435.0, 65.0, 22.0],
                "id": "obj-1194",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "triangle~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1020.0, 1435.0, 55.0, 22.0],
                "id": "obj-1195",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "tri~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1100.0, 1435.0, 26.0, 22.0],
                "id": "obj-1196",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "trunc~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1180.0, 1435.0, 42.0, 22.0],
                "id": "obj-1197",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "twist~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1260.0, 1435.0, 40.0, 22.0],
                "id": "obj-1198",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "typeroute~",
                "numoutlets": 6,
                "outlettype": ["signal", "bang", "int", "float", "", "list"],
                "patching_rect": [1340.0, 1435.0, 66.0, 22.0],
                "id": "obj-1199",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "updown~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1420.0, 1435.0, 58.0, 22.0],
                "id": "obj-1200",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "vectral~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1500.0, 1435.0, 51.0, 22.0],
                "id": "obj-1201",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "varname": "vst~",
                "viewvisibility": 0,
                "offset": [0.0, 0.0],
                "clickthrough": 0,
                "bgmode": 0,
                "border": 0,
                "text": "vst~",
                "numoutlets": 8,
                "outlettype": ["signal", "signal", "", "list", "int", "", "", ""],
                "patching_rect": [1580.0, 1435.0, 31.0, 22.0],
                "id": "obj-1202",
                "numinlets": 2,
                "save": ["#N", "vst~", "loaduniqueid", 0, ";"],
                "autosave": 1,
                "saved_object_attributes": {
                    "parameter_enable": 1,
                    "parameter_mappable": 0,
                },
                "saved_attribute_attributes": {
                    "valueof": {
                        "parameter_invisible": 1,
                        "parameter_longname": "vst~[4]",
                        "parameter_shortname": "vst~[4]",
                        "parameter_type": 3,
                    }
                },
            }
        },
        {
            "box": {
                "maxclass": "waveform~",
                "numoutlets": 6,
                "outlettype": ["float", "float", "float", "float", "list", ""],
                "patching_rect": [60.0, 1460.0, 256.0, 64.0],
                "id": "obj-1204",
                "numinlets": 5,
                "buffername": "",
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "wave~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [140.0, 1460.0, 44.0, 22.0],
                "id": "obj-1205",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "what~",
                "numoutlets": 2,
                "outlettype": ["signal", "int"],
                "patching_rect": [220.0, 1460.0, 41.0, 22.0],
                "id": "obj-1206",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "where~",
                "numoutlets": 2,
                "outlettype": ["signal", "signal"],
                "patching_rect": [300.0, 1460.0, 48.0, 22.0],
                "id": "obj-1207",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "windowed-fft~",
                "numoutlets": 2,
                "outlettype": ["signal", "signal"],
                "patching_rect": [380.0, 1460.0, 83.0, 22.0],
                "id": "obj-1208",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "zerox~",
                "numoutlets": 2,
                "outlettype": ["signal", "signal"],
                "patching_rect": [460.0, 1460.0, 45.0, 22.0],
                "id": "obj-1209",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "zigzag~",
                "numoutlets": 4,
                "outlettype": ["signal", "signal", "", "bang"],
                "patching_rect": [540.0, 1460.0, 50.0, 22.0],
                "id": "obj-1210",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "zplane~",
                "numoutlets": 4,
                "outlettype": ["list", "list", "list", "list"],
                "patching_rect": [620.0, 1460.0, 256.0, 256.0],
                "id": "obj-1212",
                "numinlets": 5,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "spigot~",
                "numoutlets": 0,
                "patching_rect": [700.0, 1460.0, 48.0, 22.0],
                "id": "obj-1213",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.broadcast",
                "numoutlets": 0,
                "patching_rect": [780.0, 1460.0, 73.0, 22.0],
                "id": "obj-1214",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.qt.broadcast",
                "numoutlets": 0,
                "patching_rect": [860.0, 1460.0, 87.0, 22.0],
                "id": "obj-1215",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "jit.qt.effect",
                "numoutlets": 0,
                "patching_rect": [940.0, 1460.0, 63.0, 22.0],
                "id": "obj-1216",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "!-~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1020.0, 1460.0, 23.0, 22.0],
                "id": "obj-1217",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "!/~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1100.0, 1460.0, 22.0, 22.0],
                "id": "obj-1218",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "!=~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1180.0, 1460.0, 26.0, 22.0],
                "id": "obj-1219",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "%~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1260.0, 1460.0, 26.0, 22.0],
                "id": "obj-1220",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "*~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1340.0, 1460.0, 20.0, 22.0],
                "id": "obj-1221",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "+~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1420.0, 1460.0, 23.0, 22.0],
                "id": "obj-1222",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "-~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1500.0, 1460.0, 20.0, 22.0],
                "id": "obj-1223",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "/~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [1580.0, 1460.0, 19.0, 22.0],
                "id": "obj-1224",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "<=~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [60.0, 1485.0, 30.0, 22.0],
                "id": "obj-1225",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "<~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [140.0, 1485.0, 23.0, 22.0],
                "id": "obj-1226",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "==~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [220.0, 1485.0, 30.0, 22.0],
                "id": "obj-1227",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": ">=~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [300.0, 1485.0, 30.0, 22.0],
                "id": "obj-1228",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": ">~",
                "numoutlets": 1,
                "outlettype": ["signal"],
                "patching_rect": [380.0, 1485.0, 23.0, 22.0],
                "id": "obj-1229",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "plugconfig",
                "numoutlets": 0,
                "patching_rect": [460.0, 1485.0, 63.0, 22.0],
                "id": "obj-1230",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "plugmidiin",
                "numoutlets": 0,
                "patching_rect": [540.0, 1485.0, 63.0, 22.0],
                "id": "obj-1231",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "plugmidiout",
                "numoutlets": 0,
                "patching_rect": [620.0, 1485.0, 70.0, 22.0],
                "id": "obj-1232",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "plugmod",
                "numoutlets": 0,
                "patching_rect": [700.0, 1485.0, 55.0, 22.0],
                "id": "obj-1233",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "plugmorph",
                "numoutlets": 0,
                "patching_rect": [780.0, 1485.0, 65.0, 22.0],
                "id": "obj-1234",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "plugmultiparam",
                "numoutlets": 0,
                "patching_rect": [860.0, 1485.0, 91.0, 22.0],
                "id": "obj-1235",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "plugstore",
                "numoutlets": 0,
                "patching_rect": [940.0, 1485.0, 58.0, 22.0],
                "id": "obj-1236",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "pp",
                "numoutlets": 0,
                "patching_rect": [1020.0, 1485.0, 22.0, 22.0],
                "id": "obj-1237",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "pptempo",
                "numoutlets": 0,
                "patching_rect": [1100.0, 1485.0, 55.0, 22.0],
                "id": "obj-1238",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "pptime",
                "numoutlets": 0,
                "patching_rect": [1180.0, 1485.0, 45.0, 22.0],
                "id": "obj-1239",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "t",
                "numoutlets": 2,
                "outlettype": ["", ""],
                "patching_rect": [1260.0, 1485.0, 18.0, 22.0],
                "id": "obj-1240",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "v",
                "numoutlets": 0,
                "patching_rect": [1340.0, 1485.0, 18.0, 22.0],
                "id": "obj-1241",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "!-",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [1420.0, 1485.0, 18.0, 22.0],
                "id": "obj-1242",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "!/",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [1500.0, 1485.0, 18.0, 22.0],
                "id": "obj-1243",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "!=",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [1580.0, 1485.0, 19.0, 22.0],
                "id": "obj-1244",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "%",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [60.0, 1510.0, 19.0, 22.0],
                "id": "obj-1245",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "&",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [140.0, 1510.0, 18.0, 22.0],
                "id": "obj-1246",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "&&",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [220.0, 1510.0, 25.0, 22.0],
                "id": "obj-1247",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "*",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [300.0, 1510.0, 18.0, 22.0],
                "id": "obj-1248",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "+",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [380.0, 1510.0, 18.0, 22.0],
                "id": "obj-1249",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "-",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [460.0, 1510.0, 18.0, 22.0],
                "id": "obj-1250",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "/",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [540.0, 1510.0, 18.0, 22.0],
                "id": "obj-1251",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "<",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [620.0, 1510.0, 18.0, 22.0],
                "id": "obj-1252",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "<<",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [700.0, 1510.0, 23.0, 22.0],
                "id": "obj-1253",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "<=",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [780.0, 1510.0, 23.0, 22.0],
                "id": "obj-1254",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "==",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [860.0, 1510.0, 23.0, 22.0],
                "id": "obj-1255",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": ">",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [940.0, 1510.0, 18.0, 22.0],
                "id": "obj-1256",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": ">=",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [1020.0, 1510.0, 23.0, 22.0],
                "id": "obj-1257",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": ">>",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [1100.0, 1510.0, 23.0, 22.0],
                "id": "obj-1258",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "|",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [1180.0, 1510.0, 18.0, 22.0],
                "id": "obj-1259",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "||",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [1260.0, 1510.0, 18.0, 22.0],
                "id": "obj-1260",
                "numinlets": 2,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "r",
                "numoutlets": 1,
                "outlettype": [""],
                "patching_rect": [1340.0, 1510.0, 18.0, 22.0],
                "id": "obj-1261",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "s",
                "numoutlets": 0,
                "patching_rect": [1420.0, 1510.0, 18.0, 22.0],
                "id": "obj-1262",
                "numinlets": 0,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "xbendin2",
                "numoutlets": 3,
                "outlettype": ["int", "int", "int"],
                "patching_rect": [1500.0, 1510.0, 57.0, 22.0],
                "id": "obj-1263",
                "numinlets": 1,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "xbendout2",
                "numoutlets": 1,
                "outlettype": ["int"],
                "patching_rect": [1580.0, 1510.0, 65.0, 22.0],
                "id": "obj-1264",
                "numinlets": 3,
            }
        },
        {
            "box": {
                "maxclass": "newobj",
                "text": "b",
                "numoutlets": 2,
                "outlettype": ["bang", "bang"],
                "patching_rect": [60.0, 1535.0, 18.0, 22.0],
                "id": "obj-1265",
                "numinlets": 1,
            }
        },
    ],
    "appversion": {
        "major": 8,
        "minor": 6,
        "revision": 0,
        "architecture": "x64",
        "modernui": 1,
    },
    "classnamespace": "box",
}
