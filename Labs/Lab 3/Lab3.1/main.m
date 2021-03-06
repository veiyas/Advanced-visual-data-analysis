im = im2double(imread('11.jpg'));

imHSV = rgb2hsv(im);

[H_hist, ~] = histcounts(reshape(imHSV(:,:,1), 1, size(imHSV,1)*size(imHSV,2)), [0:1/360:1]);
[S_hist, ~] = histcounts(reshape(imHSV(:,:,2), 1, size(imHSV,1)*size(imHSV,2)), [0:1/100:1]);
[V_hist, ~] = histcounts(reshape(imHSV(:,:,3), 1, size(imHSV,1)*size(imHSV,2)), [0:1/100:1]);

BW = edge(rgb2gray(im), 'canny');
[houghRes,T,R] = hough(BW, 'Theta', -90:0.5:89);

lbpTest = extractLBPFeatures(rgb2gray(im));


%%
chosenBase = 11;
if chosenBase < 10
    chosenBasePrefix = strcat('0',int2str(chosenBase));
else
    chosenBasePrefix = int2str(chosenBase);
end
allPathsPrefix = ['010203040506070809101112'];
paths = erase(allPathsPrefix, chosenBasePrefix);

S = get_features(imread(strcat(chosenBasePrefix, '.jpg')));
baseFVec = get_feature_vector(S);

pathSuffix = '.jpg';
fullPath = '';

lowestDiffs = [];
for i = 1:2:size(paths,2)
    fullPath = strcat(paths(i:i+1), pathSuffix);
    S = get_features(imread(fullPath));
    
    fVec = get_feature_vector(S);
    lowestDiffs((i+1)/2,:) = [norm(baseFVec - fVec)/1000];
end

[B, I] = sort(lowestDiffs);
sortedSimilarity = I + double(I >= chosenBase)


%%
function [feature_vector] = get_feature_vector(S)
    feature_vector = [S.H S.S S.V S.H_mean S.S_mean S.V_mean S.H_std S.S_std S.V_std S.LBP];
end


