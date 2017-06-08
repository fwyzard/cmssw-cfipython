import FWCore.ParameterSet.Config as cms

FastjetJetProducer = cms.EDProducer('FastjetJetProducer',
  useMassDropTagger = cms.bool(False),
  useFiltering = cms.bool(False),
  useDynamicFiltering = cms.bool(False),
  useTrimming = cms.bool(False),
  usePruning = cms.bool(False),
  useCMSBoostedTauSeedingAlgorithm = cms.bool(False),
  useKtPruning = cms.bool(False),
  useConstituentSubtraction = cms.bool(False),
  useSoftDrop = cms.bool(False),
  correctShape = cms.bool(False),
  UseOnlyVertexTracks = cms.bool(False),
  UseOnlyOnePV = cms.bool(False),
  muCut = cms.double(-1),
  yCut = cms.double(-1),
  rFilt = cms.double(-1),
  rFiltFactor = cms.double(-1),
  trimPtFracMin = cms.double(-1),
  zcut = cms.double(-1),
  rcut_factor = cms.double(-1),
  csRho_EtaMax = cms.double(-1),
  csRParam = cms.double(-1),
  beta = cms.double(-1),
  R0 = cms.double(-1),
  gridMaxRapidity = cms.double(-1),
  gridSpacing = cms.double(-1),
  DzTrVtxMax = cms.double(999999),
  DxyTrVtxMax = cms.double(999999),
  MaxVtxZ = cms.double(15),
  subjetPtMin = cms.double(-1),
  muMin = cms.double(-1),
  muMax = cms.double(-1),
  yMin = cms.double(-1),
  yMax = cms.double(-1),
  dRMin = cms.double(-1),
  dRMax = cms.double(-1),
  maxDepth = cms.int32(-1),
  nFilt = cms.int32(-1),
  MinVtxNdof = cms.int32(5),
  jetCollInstanceName = cms.string(''),
  src = cms.InputTag('particleFlow'),
  srcPVs = cms.InputTag(''),
  jetType = cms.string('PFJet'),
  jetAlgorithm = cms.string('AntiKt'),
  rParam = cms.double(0.4),
  inputEtMin = cms.double(0),
  inputEMin = cms.double(0),
  jetPtMin = cms.double(5),
  doPVCorrection = cms.bool(False),
  doAreaFastjet = cms.bool(False),
  doRhoFastjet = cms.bool(False),
  doPUOffsetCorr = cms.bool(False),
  subtractorName = cms.string(''),
  useExplicitGhosts = cms.bool(False),
  doAreaDiskApprox = cms.bool(False),
  voronoiRfact = cms.double(-0.9),
  Rho_EtaMax = cms.double(4.4),
  Ghost_EtaMax = cms.double(5),
  Active_Area_Repeats = cms.int32(1),
  GhostArea = cms.double(0.01),
  restrictInputs = cms.bool(False),
  maxInputs = cms.uint32(1),
  writeCompound = cms.bool(False),
  doFastJetNonUniform = cms.bool(False),
  useDeterministicSeed = cms.bool(False),
  minSeed = cms.uint32(14327),
  verbosity = cms.int32(0),
  puWidth = cms.double(0),
  nExclude = cms.uint32(0),
  maxBadEcalCells = cms.uint32(9999999),
  maxBadHcalCells = cms.uint32(9999999),
  maxProblematicEcalCells = cms.uint32(9999999),
  maxProblematicHcalCells = cms.uint32(9999999),
  maxRecoveredEcalCells = cms.uint32(9999999),
  maxRecoveredHcalCells = cms.uint32(9999999),
  puCenters = cms.vdouble(),
  puPtMin = cms.double(10),
  nSigmaPU = cms.double(1),
  radiusPU = cms.double(0.5),
  sumRecHits = cms.bool(False)
)
