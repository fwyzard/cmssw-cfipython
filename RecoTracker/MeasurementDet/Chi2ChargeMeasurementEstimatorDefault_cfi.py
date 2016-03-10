import FWCore.ParameterSet.Config as cms

Chi2ChargeMeasurementEstimatorDefault = cms.ESProducer('Chi2ChargeMeasurementEstimatorESProducer',
  MaxChi2 = cms.double(30),
  nSigma = cms.double(3),
  MaxDisplacement = cms.double(0.5),
  MaxSagitta = cms.double(2),
  MinimalTolerance = cms.double(0.5),
  ComponentName = cms.string('Chi2Charge'),
  pTChargeCutThreshold = cms.double(-1),
  clusterChargeCut = cms.PSet(
    value = cms.double(1620)
  ),
  appendToDataLabel = cms.string('')
)
