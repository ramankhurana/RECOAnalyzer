import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
process.MessageLogger.cerr.FwkReport.reportEvery = 10

process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = "80X_dataRun2_Prompt_ICHEP16JEC_v0"

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/00C89AE8-2957-E611-9E24-0CC47A78A340.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/00CD6A8B-6B57-E611-B4DD-0025905A6118.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/042501E5-7457-E611-B138-0025905B8562.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/04519520-2957-E611-A111-0025905B85CA.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/061DF628-2957-E611-B5EE-0025905A612A.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/066619F2-2A57-E611-BB29-0CC47A4C8F10.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/06D7E051-6F57-E611-A115-0025905A6132.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/08C4F52C-6D57-E611-B4C8-0025905A60A8.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/0AB2EDF3-3157-E611-B533-0025905A608A.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/0C70291E-4357-E611-A0F8-0CC47A4D764C.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/12B4D622-3857-E611-84BE-0CC47A4D7670.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/14478733-4157-E611-BD4F-0025905B8562.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/1AF53C33-4157-E611-B27F-0CC47A4D766C.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/1CFD4EB5-2A57-E611-B18D-0CC47A78A456.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/1E48CEDF-3D57-E611-9690-0CC47A4D7618.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/207B2F91-4B57-E611-8BED-0025905B8610.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/22685212-4557-E611-89F4-0025905B85EE.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/229F1757-4A57-E611-9264-003048FFD798.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/22E9B4B2-7057-E611-9520-003048FFD79E.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/2A59A572-2557-E611-8C1A-0025905A60BE.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/2C14E445-4C57-E611-A6E2-0CC47A78A458.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/2C639094-3E57-E611-9E3F-0CC47A4D768E.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/2ECE9000-5157-E611-ACC2-0025905A60D6.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/32481B83-2F57-E611-87E9-0025905B85B2.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/344E6E7B-4557-E611-A060-0CC47A4D766C.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/3C2C6675-3157-E611-83D5-0CC47A78A440.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/3E0F044E-6757-E611-AB92-0CC47A4D768C.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/3EC6EEB6-7057-E611-AB53-0025905A60D0.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/4651A64C-4A57-E611-9527-0025905A6084.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/4A255927-4957-E611-8A90-0025905B8574.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/4A99E4A0-3E57-E611-BC79-0025905B85EE.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/4CB57A68-6D57-E611-8D6F-002618FDA265.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/4CEC75A7-6A57-E611-B0E8-0CC47A4D7650.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/4E603002-4457-E611-84E2-003048FFD75A.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/4ED3B02A-4657-E611-8C2C-0CC47A4C8E98.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/502DDF54-6957-E611-B32C-0CC47A4C8F10.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/56877864-3857-E611-A9B2-002618FDA207.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/5694CE78-7557-E611-B9E0-0CC47A4C8EC8.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/56EC4E25-6E57-E611-A603-0CC47A78A478.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/5A17C555-4D57-E611-938A-0CC47A4C8E86.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/5C9B065C-2A57-E611-B97D-0CC47A745250.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/5EF47F0D-2C57-E611-A905-0025905B85FC.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/623623BB-2B57-E611-BC66-0CC47A78A458.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/62FA4631-7357-E611-9A73-0025905A6132.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/68935BFE-3D57-E611-A7CC-0025905A6084.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/6A841ED9-4357-E611-9A2C-0CC47A4C8ECA.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/6AD5D6AB-3F57-E611-A46F-0025905A608C.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/6C1FDA0F-2857-E611-A5BD-0025905A6064.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/7A5758A9-6A57-E611-B669-0CC47A4D767E.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/7E02827F-6B57-E611-B524-0025905A60D6.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/802D9E93-4557-E611-9A4D-0025905AA9F0.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/82182E39-7357-E611-AC74-003048FF9ABC.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/846EF390-3F57-E611-B37A-0CC47A4C8E96.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/84DDEA96-4B57-E611-9BAF-0025905A612E.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/86FF4712-2757-E611-9BCE-0CC47A4D75EC.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/8AA38300-2D57-E611-9BC6-0CC47A78A4B0.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/8ED78606-6957-E611-916D-0025905B855C.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/98F1A603-2857-E611-864E-0025905B8596.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/9C8F26EC-2757-E611-89F6-0CC47A4D76B6.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/9EB6A42B-3C57-E611-8CF1-0025905A497A.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/A003B7C7-4357-E611-8C5A-0025905B85B6.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/A00A727E-2F57-E611-8964-0CC47A4C8EC6.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/A07B6CFF-3D57-E611-AD81-0CC47A4C8EBA.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/A2983AAD-2A57-E611-9F51-0CC47A78A2EC.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/A4C6511F-2B57-E611-A361-0025905B856E.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/A6580CF9-3457-E611-89DB-0025905A6088.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/AA5BC8FB-7357-E611-8791-0025905A6092.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/AAAFF525-4157-E611-805A-0CC47A4D7602.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/B2BBFE13-4557-E611-9395-0025905A6118.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/B638DA32-6F57-E611-8BF3-0CC47A4D76B6.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/B8C8072E-4657-E611-82D8-0025905A606A.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/BE405EFD-3D57-E611-9A41-0CC47A4C8E98.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/BECF41EF-2957-E611-B890-0CC47A4D765A.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/C030883C-4257-E611-9ADB-0025905B85FC.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/C0E8A777-3957-E611-B063-0CC47A4C8E26.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/C0F1221F-6D57-E611-98AB-0CC47A4D76BE.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/C893A130-4C57-E611-BFCF-0CC47A4D7614.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/CCA9023D-3857-E611-89B1-0025905B8562.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/CEECEB31-4257-E611-B49C-0025905B85EE.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/D0FDF201-3057-E611-892D-0025905A6094.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/D6C2F719-3957-E611-A5A6-0025905B85CA.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/DA125462-3157-E611-B6E2-0CC47A4D75F6.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/DED6656B-7157-E611-83AE-0CC47A4D76D6.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/EAB1146C-7157-E611-B16C-0CC47A4D7686.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/EC0E0E28-4957-E611-8E9C-0025905B856E.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/EC866144-2F57-E611-9599-0025905A607E.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/F21BB61C-4957-E611-93BC-0025905A60F8.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/F2777E97-2C57-E611-9257-0025905B8610.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/F4FDB42D-7357-E611-A983-0CC47A78A42E.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/10000/FCA315F7-3157-E611-9987-0025905A6136.root'
    )
)

process.load('JetMETCorrections.Configuration.JetCorrectors_cff')

process.ak4PFchsCorrectedJets   = cms.EDProducer('CorrectedPFJetProducer',
    src         = cms.InputTag('ak4PFJetsCHS'),
    correctors  = cms.VInputTag('ak4PFCHSL1FastL2L3Corrector')
)

process.load("PhysicsTools/JetMCAlgos/HadronAndPartonSelector_cfi")  
process.load("PhysicsTools/JetMCAlgos/AK4PFJetsMCFlavourInfos_cfi")
#process.ak4JetFlavourInfos.jets = cms.InputTag("ak4PFchsCorrectedJets")
process.ak4JetFlavourInfos.jets = cms.InputTag("ak4PFJetsCHS")

process.check = cms.EDAnalyzer("RECOAnalyzer",
    vertices = cms.InputTag("offlinePrimaryVertices"),
    #jets = cms.InputTag("ak4PFchsCorrectedJets"),
    jets = cms.InputTag("ak4PFJetsCHS"),
    btags = cms.InputTag("pfCombinedInclusiveSecondaryVertexV2BJetTags"),
    flavorinfo = cms.InputTag("ak4JetFlavourInfos"),
    genparticles = cms.InputTag("genParticles"),
    electrons = cms.InputTag("gedGsfElectrons"),
    beamspot = cms.InputTag("offlineBeamSpot"),
    conversions = cms.InputTag("particleFlowEGamma"),
    muons = cms.InputTag("muons"),
    debug = cms.bool(False)
)

process.TFileService = cms.Service("TFileService", 
    fileName = cms.string("histo_elgun_pu200.root"),
    closeFileFast = cms.untracked.bool(True)
)

#process.p = cms.Path(process.ak4PFCHSL1FastL2L3CorrectorChain + process.ak4PFchsCorrectedJets + process.selectedHadronsAndPartons + process.ak4JetFlavourInfos + process.check)
process.p = cms.Path(process.selectedHadronsAndPartons + process.ak4JetFlavourInfos + process.check)
