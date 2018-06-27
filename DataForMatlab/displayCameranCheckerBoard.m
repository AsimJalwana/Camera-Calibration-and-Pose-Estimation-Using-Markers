function status = displayCameranCheckerBoard()
    LoadedData = load('cameraParameterFromPython.mat');
    kinectParams = cameraParameters('IntrinsicMatrix', double(LoadedData.IntrinicMatrix), ...
                                'RadialDistortion', double(LoadedData.RadialDistortion), ...
                                'TangentialDistortion', double(LoadedData.TangentialDistortion), ...
                                'RotationVectors', double(LoadedData.RotationVectors),  ...
                                'TranslationVectors', double(LoadedData.TranslationVectors), ...
                                'WorldPoints', double(LoadedData.WorldPoints));

    figure(1);
    subplot(1,2,1);
    showExtrinsics(kinectParams,'patternCentric');
    title('Moving Camera')
    subplot(1,2,2);
    showExtrinsics(kinectParams);
    title('Static Camera')
    pause(5);
    status = 'Cool Display :)';
end

