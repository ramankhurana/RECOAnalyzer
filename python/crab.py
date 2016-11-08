from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.section_('JobType')
config.JobType.psetName = 'runEff.py'
config.JobType.pluginName = 'Analysis'
config.section_('Data')
#config.Data.inputDataset = '/RelValZMM_13/CMSSW_8_1_0_pre9-PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/GEN-SIM-RECO'
#config.Data.inputDataset = '/RelValZMM_13/CMSSW_8_1_0_pre9-PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/GEN-SIM-RECO'
#config.Data.inputDataset = '/RelValZMM_13/CMSSW_8_1_0_pre9-PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/GEN-SIM-RECO'
#config.Data.inputDataset = '/RelValTTbar_14TeV/CMSSW_8_1_0_pre9-PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/GEN-SIM-RECO'
#config.Data.inputDataset = '/RelValTTbar_14TeV/CMSSW_8_1_0_pre9-PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/GEN-SIM-RECO'
#config.Data.inputDataset = '/RelValTTbar_14TeV/CMSSW_8_1_0_pre9-PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/GEN-SIM-RECO'
#config.Data.inputDataset = '/RelValSingleElectronPt35Extended/CMSSW_8_1_0_pre9-PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/GEN-SIM-RECO'
#config.Data.inputDataset = '/RelValSingleElectronPt35Extended/CMSSW_8_1_0_pre9-PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/GEN-SIM-RECO'
config.Data.inputDataset = '/RelValSingleElectronPt35Extended/CMSSW_8_1_0_pre9-PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU200-v1/GEN-SIM-RECO'
config.Data.publication = False
config.Data.unitsPerJob = 1
config.Data.splitting = 'FileBased'
#config.Data.lumiMask = 'Cert_271036-275783_13TeV_PromptReco_Collisions16_JSON.txt'
#config.Data.runRange = '271036-275125'
config.section_('User')
config.section_('Site')
config.Site.storageSite = 'T3_US_FNALLPC'
