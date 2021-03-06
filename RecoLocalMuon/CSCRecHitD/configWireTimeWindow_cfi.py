import FWCore.ParameterSet.Config as cms

configWireTimeWindow = cms.EDProducer('CSCRecHitDProducer',
  CSCStripPeakThreshold = cms.double(10),
  CSCStripClusterChargeCut = cms.double(25),
  CSCStripxtalksOffset = cms.double(0.03),
  UseAverageTime = cms.bool(False),
  UseParabolaFit = cms.bool(False),
  UseFivePoleFit = cms.bool(True),
  CSCWireClusterDeltaT = cms.int32(1),
  CSCUseCalibrations = cms.bool(True),
  CSCUseStaticPedestals = cms.bool(False),
  CSCNoOfTimeBinsForDynamicPedestal = cms.int32(2),
  wireDigiTag = cms.InputTag('muonCSCDigis', 'MuonCSCWireDigi'),
  stripDigiTag = cms.InputTag('muonCSCDigis', 'MuonCSCStripDigi'),
  readBadChannels = cms.bool(True),
  readBadChambers = cms.bool(True),
  CSCUseTimingCorrections = cms.bool(True),
  CSCUseGasGainCorrections = cms.bool(True),
  CSCDebug = cms.untracked.bool(False),
  CSCstripWireDeltaTime = cms.int32(8),
  CSCStripClusterSize = cms.untracked.int32(3),
  XTasymmetry_ME1a = cms.double(0.023),
  XTasymmetry_ME1b = cms.double(0.01),
  XTasymmetry_ME12 = cms.double(0.015),
  XTasymmetry_ME13 = cms.double(0.02),
  XTasymmetry_ME21 = cms.double(0.023),
  XTasymmetry_ME22 = cms.double(0.023),
  XTasymmetry_ME31 = cms.double(0.023),
  XTasymmetry_ME32 = cms.double(0.023),
  XTasymmetry_ME41 = cms.double(0.023),
  ConstSyst_ME1a = cms.double(0.01),
  ConstSyst_ME1b = cms.double(0.02),
  ConstSyst_ME12 = cms.double(0.02),
  ConstSyst_ME13 = cms.double(0.03),
  ConstSyst_ME21 = cms.double(0.03),
  ConstSyst_ME22 = cms.double(0.03),
  ConstSyst_ME31 = cms.double(0.03),
  ConstSyst_ME32 = cms.double(0.03),
  ConstSyst_ME41 = cms.double(0.03),
  NoiseLevel_ME1a = cms.double(9),
  NoiseLevel_ME1b = cms.double(6),
  NoiseLevel_ME12 = cms.double(7),
  NoiseLevel_ME13 = cms.double(4),
  NoiseLevel_ME21 = cms.double(5),
  NoiseLevel_ME22 = cms.double(7),
  NoiseLevel_ME31 = cms.double(5),
  NoiseLevel_ME32 = cms.double(7),
  NoiseLevel_ME41 = cms.double(5),
  CSCUseReducedWireTimeWindow = cms.bool(False),
  CSCWireTimeWindowLow = cms.int32(0),
  CSCWireTimeWindowHigh = cms.int32(15)
)
