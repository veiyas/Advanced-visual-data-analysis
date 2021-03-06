function [features_struct] = get_features(im)
im = im2double(im);

imHSV = rgb2hsv(im);

[H_hist, ~] = histcounts(reshape(imHSV(:,:,1), 1, size(imHSV,1)*size(imHSV,2)), [0:1/360:1]);
[S_hist, ~] = histcounts(reshape(imHSV(:,:,2), 1, size(imHSV,1)*size(imHSV,2)), [0:1/100:1]);
[V_hist, ~] = histcounts(reshape(imHSV(:,:,3), 1, size(imHSV,1)*size(imHSV,2)), [0:1/100:1]);

H_hist = H_hist ./ (size(imHSV,1)*size(imHSV,2));
S_hist = S_hist ./ (size(imHSV,1)*size(imHSV,2));
V_hist = V_hist ./ (size(imHSV,1)*size(imHSV,2));

H_mean = mean(mean(imHSV(:,:,1)));
S_mean = mean(mean(imHSV(:,:,2)));
V_mean = mean(mean(imHSV(:,:,3)));

H_std = std(reshape(imHSV(:,:,1), 1, size(imHSV,1)*size(imHSV,2)));
S_std = std(reshape(imHSV(:,:,2), 1, size(imHSV,1)*size(imHSV,2)));
V_std = std(reshape(imHSV(:,:,3), 1, size(imHSV,1)*size(imHSV,2)));

lbp = extractLBPFeatures(rgb2gray(im));

features_struct = struct('H',H_hist,'S', S_hist, 'V', V_hist,...
    'H_mean', H_mean, 'S_mean', S_mean, 'V_mean', V_mean,...
    'H_std', H_std, 'S_std', S_std, 'V_std', V_std, 'LBP', lbp);
end

