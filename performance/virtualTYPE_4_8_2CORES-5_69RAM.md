moai@demuxer1:~/demucs-client$ sudo python3 keepAlive.py
[sudo] password for moai:

CLIENT [running]

Not any Task Attempts: 8 times
Checking 30secondMusic.mp3
        File Size [OK]
        File mimetype [OK]
===================DOWNLOADING beta========================

 @@ RUNNING DEMUCS AUTOMAGIC @@
 50%|█████████████████████████████████████                                     | 33.0/66.0 [00:18<00:18,  1.77seconds/s][W NNPACK.cpp:51] Could not initialize NNPACK! Reason: Unsupported hardware.
100%|██████████████████████████████████████████████████████████████████████████| 66.0/66.0 [00:19<00:00,  3.33seconds/s]
100%|██████████████████████████████████████████████████████████████████████████| 66.0/66.0 [00:18<00:00,  3.49seconds/s]
100%|██████████████████████████████████████████████████████████████████████████| 66.0/66.0 [00:20<00:00,  3.22seconds/s]
100%|██████████████████████████████████████████████████████████████████████████| 66.0/66.0 [00:19<00:00,  3.44seconds/s]
Selected model is a bag of 4 models. You will see that many progress bars per track.
Separated tracks will be stored in /home/moai/demucs-client/separated/mdx_extra_q
Separating track input/30secondMusic.mp3

-->End of the task next in 5 seconds
Not any Task Attempts: 16 times
Checking 30secondMusic.mp3
        File Size [OK]
        File mimetype [OK]
===================DOWNLOADING beta========================

 @@ RUNNING DEMUCS AUTOMAGIC @@
 50%|█████████████████████████████████████                                     | 33.0/66.0 [00:16<00:16,  1.94seconds/s][W NNPACK.cpp:51] Could not initialize NNPACK! Reason: Unsupported hardware.
100%|██████████████████████████████████████████████████████████████████████████| 66.0/66.0 [00:18<00:00,  3.64seconds/s]
100%|██████████████████████████████████████████████████████████████████████████| 66.0/66.0 [00:18<00:00,  3.52seconds/s]
100%|██████████████████████████████████████████████████████████████████████████| 66.0/66.0 [00:18<00:00,  3.51seconds/s]
100%|██████████████████████████████████████████████████████████████████████████| 66.0/66.0 [00:18<00:00,  3.48seconds/s]
Selected model is a bag of 4 models. You will see that many progress bars per track.
Separated tracks will be stored in /home/moai/demucs-client/separated/mdx_extra_q
Separating track input/30secondMusic.mp3

-->End of the task next in 5 seconds
Not any Task Attempts: 20 times


# AVENGED SEVENFOLD

Not any Task Attempts: 124 times
Checking avanegedsevenfoldhailtotheking.mp3
        File Size [OK]
        File mimetype [OK]
===================DOWNLOADING beta========================

 @@ RUNNING DEMUCS AUTOMAGIC @@
100%|████████████████████████████████████████████████████████████████████████| 330.0/330.0 [04:00<00:00,  1.37seconds/s]
100%|████████████████████████████████████████████████████████████████████████| 330.0/330.0 [05:34<00:00,  1.01s/seconds]
100%|████████████████████████████████████████████████████████████████████████| 330.0/330.0 [07:03<00:00,  1.28s/seconds]
 10%|███████▎                                                                 | 33.0/330.0 [01:38<14:47,  2.99s/seconds]
 20%|██████████████▌                                                          | 66.0/330.0 [03:05<12:15,  2.79s/seconds]^C^CError in sys.excepthook:
Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/apport_python_hook.py", line 34, in apport_excepthook
    def apport_excepthook(exc_type, exc_obj, exc_tb):
KeyboardInterrupt

Original exception was:
Traceback (most recent call last):
  File "/home/moai/demucs-client/keepAlive.py", line 7, in <module>
    cliente.run()
  File "/home/moai/demucs-client/client.py", line 32, in run
    demucs.demucs_separate(file_name,'output')
  File "/home/moai/demucs-client/runner.py", line 16, in demucs_separate
    command_output = os.popen(f'python3 -m demucs -d cpu input/{input}').read()
KeyboardInterrupt
 20%|██████████████▌                                                          | 66.0/330.0 [04:18<17:12,  3.91s/seconds]
Traceback (most recent call last):
  File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/usr/lib/python3.10/runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "/root/.local/lib/python3.10/site-packages/demucs/__main__.py", line 10, in <module>
    main()
  File "/root/.local/lib/python3.10/site-packages/demucs/separate.py", line 153, in main
    sources = apply_model(model, wav[None], device=args.device, shifts=args.shifts,
  File "/root/.local/lib/python3.10/site-packages/demucs/apply.py", line 167, in apply_model
    out = apply_model(sub_model, mix, **kwargs)
  File "/root/.local/lib/python3.10/site-packages/demucs/apply.py", line 208, in apply_model
    chunk_out = future.result()
  File "/root/.local/lib/python3.10/site-packages/demucs/utils.py", line 119, in result
    return self.func(*self.args, **self.kwargs)
  File "/root/.local/lib/python3.10/site-packages/demucs/apply.py", line 224, in apply_model
    shifted_out = apply_model(model, shifted, **kwargs)
  File "/root/.local/lib/python3.10/site-packages/demucs/apply.py", line 236, in apply_model
    out = model(padded_mix)
  File "/root/.local/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1130, in _call_impl
    return forward_call(*input, **kwargs)
  File "/root/.local/lib/python3.10/site-packages/demucs/hdemucs.py", line 768, in forward
    x = self._ispec(zout, length)
  File "/root/.local/lib/python3.10/site-packages/demucs/hdemucs.py", line 616, in _ispec
    x = ispectro(z, hl, length=le)
  File "/root/.local/lib/python3.10/site-packages/demucs/spec.py", line 32, in ispectro
    x = th.istft(z,
KeyboardInterrupt

# NEW COMMAND ARGUMENT -n 83fc094f

moai@demuxer1:~/demucs-client$ sudo python3 keepAlive.py
[sudo] password for moai:

CLIENT [running]

Not any Task Attempts: 18 times
Checking avanegedsevenfoldhailtotheking.mp3
        File Size [OK]
        File mimetype [OK]
===================DOWNLOADING beta========================

 @@ RUNNING DEMUCS AUTOMAGIC @@
 25%|██████████████████▎                                                      | 84.0/336.0 [02:14<06:44,  1.60s/seconds]
^C^C^CTraceback (most recent call last):
  File "/home/moai/demucs-client/keepAlive.py", line 7, in <module>
    cliente.run()
  File "/home/moai/demucs-client/client.py", line 32, in run
    demucs.demucs_separate(file_name,'output')
  File "/home/moai/demucs-client/runner.py", line 16, in demucs_separate
    command_output = os.popen(f'python3 -m demucs -n 83fc094f -d cpu input/{input}').read()
KeyboardInterrupt


# AUMENTAR LA MEMORIA RAM A 10.000 MB



CLIENT [running]

Not any Task Attempts: 7 times
Checking avanegedsevenfoldhailtotheking.mp3
        File Size [OK]
        File mimetype [OK]
===================DOWNLOADING beta========================

 @@ RUNNING DEMUCS AUTOMAGIC @@
 25%|██████████████████▎                                                      | 84.0/336.0 [01:04<03:13,  1.30seconds/s]^CTraceback (most recent call last):
  File "/home/moai/demucs-client/keepAlive.py", line 7, in <module>
    cliente.run()
  File "/home/moai/demucs-client/client.py", line 32, in run
    demucs.demucs_separate(file_name,'output')
  File "/home/moai/demucs-client/runner.py", line 16, in demucs_separate
    command_output = os.popen(f'python3 -m demucs -n 83fc094f -d cpu input/{input}').read()
KeyboardInterrupt


# BACK TO WITHOUT -n AND NOW WITH -j 2 DUE TO MORE RAM 

CLIENT [running]

Not any Task Attempts: 15 times
Checking avanegedsevenfoldhailtotheking.mp3
        File Size [OK]
        File mimetype [OK]
===================DOWNLOADING beta========================

 @@ RUNNING DEMUCS AUTOMAGIC @@
100%|████████████████████████████████████████████████████████████████████████| 330.0/330.0 [03:22<00:00,  1.63seconds/s]
100%|████████████████████████████████████████████████████████████████████████| 330.0/330.0 [03:28<00:00,  1.59seconds/s]
100%|████████████████████████████████████████████████████████████████████████| 330.0/330.0 [04:25<00:00,  1.24seconds/s]
100%|████████████████████████████████████████████████████████████████████████| 330.0/330.0 [03:41<00:00,  1.49seconds/s]
Selected model is a bag of 4 models. You will see that many progress bars per track.
Separated tracks will be stored in /home/moai/demucs-client/separated/mdx_extra_q
Separating track input/avanegedsevenfoldhailtotheking.mp3

-->End of the task next in 5 seconds
Not any Task Attempts: 20 times

